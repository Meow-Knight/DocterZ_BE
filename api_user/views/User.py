import json

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import UserPermission
from api_base.views import BaseViewSet
from api_user.models import User
from api_user.serializers.User import RegisterUserSerializer, EditUserSerializer
from api_user.services import UserService


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [UserPermission]
    permission_map = {
        "login": [],
        "signup": []
    }
    serializer_map = {
        "edit_own_profile": EditUserSerializer
    }

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        response_data = UserService.signup(request)
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['put'])
    def edit_own_profile(self, request, *args, **kwargs):
        account = request.user
        user = User.objects.get(account=account)

        request_data = request.data.dict()

        insurance_data = request_data.get('insurance')
        if insurance_data:
            insurance_data = json.loads(insurance_data)
            request_data['insurance'] = insurance_data
        serializer = self.get_serializer(user, data=request_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            response_data = serializer.data
            response_data['avatar'] = user.account.avatar
            return Response(response_data)
