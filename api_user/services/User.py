from django.db import transaction

from api_account.constants import RoleData
from api_account.serializers import AccountSerializer
from api_account.services import AccountService
from api_user.serializers import RegisterUserSerializer


class UserService:
    @classmethod
    @transaction.atomic
    def signup(cls, request):
        user_data = request.data
        user_data['role'] = RoleData.USER.value.get('id')
        account_serializer = AccountSerializer(data=user_data)
        if account_serializer.is_valid(raise_exception=True):
            account = account_serializer.save()
            user_data['account'] = account.id.hex
            serializer = RegisterUserSerializer(data=user_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return AccountService.get_login_info(account)
