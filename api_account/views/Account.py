from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_account.models import Account
from api_account.serializers import AccountSerializer
from api_account.services import AccountService
from api_base.views import BaseViewSet


class AccountViewSet(BaseViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    permission_map = {
        "login": [],
        "signup": [],
        "change_password": [IsAuthenticated]
    }

    @action(detail=False, methods=['post'])
    def login(self, request):
        user_request_data = request.data
        username = user_request_data.get("username")
        password = user_request_data.get("password")

        account = Account.objects.filter(username=username)
        if account.exists():
            account = account.first()
            if not account.is_activate:
                return Response({"detail": "This account is deactivated"}, status=status.HTTP_400_BAD_REQUEST)
            if check_password(password, account.password):
                response_data = AccountService.get_login_info(account)
                return Response(response_data)
        return Response({"details": "Invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def change_password(self, request):
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not current_password or not new_password:
            error_response = {}
            if not current_password:
                error_response['current_password'] = "Trường này là bắt buộc"
            if not new_password:
                error_response['new_password'] = "Trường này là bắt buộc"
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

        is_changed = AccountService.change_password(request.user, current_password, new_password)
        if is_changed:
            return Response({"message": "Mật khẩu đã được thay đổi"})
        return Response({"message": "Mật khẩu hiện tại không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)
