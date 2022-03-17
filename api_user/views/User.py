from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.constants import RoleData
from api_account.permissions import UserPermission, AdminPermission
from api_account.services import AccountService
from api_base.views import BaseViewSet
from api_user.models import User
from api_user.serializers.User import RegisterUserSerializer
from api_user.services import UserService


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [UserPermission]
    permission_map = {
        "login": [],
        "signup": [AdminPermission]
    }

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        response_data = UserService.signup(request)
        return Response(response_data, status=status.HTTP_201_CREATED)
