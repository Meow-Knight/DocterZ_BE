from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_account.models import Account
from api_account.serializers import AccountSerializer
from api_base.views import BaseViewSet


class AccountViewSet(BaseViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    permission_map = {
        "login": [],
        "signup": []
    }

    @action(detail=False, methods=['post'])
    def login(self, request):
        user_request_data = request.data
        username = user_request_data.get("username")
        password = user_request_data.get("password")

        account = Account.objects.filter(username=username)
        if account.exists():
            account = account.first()
            if not account.is_active:
                return Response({"detail": "This account is deactivated"}, status=status.HTTP_400_BAD_REQUEST)
            if check_password(password, account.password):
                token = RefreshToken.for_user(account)
                response = {
                    'id': str(account.id),
                    'email': account.email,
                    'role': account.role.name,
                    'access_token': str(token.access_token),
                    'refresh_token': str(token)
                }
                return Response(response)
        return Response({"details": "Invalid username/password"}, status=status.HTTP_400_BAD_REQUEST)
