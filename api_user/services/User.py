from django.db import transaction
from rest_framework.exceptions import ValidationError


from api_account.constants import RoleData
from api_account.services import AccountService
from api_user.serializers import RegisterUserSerializer


class UserService:
    @classmethod
    @transaction.atomic
    def signup(cls, request):
        user_data = request.data
        if not user_data.get('account'):
            raise ValidationError({"detail": "account field is required"})
        user_data.get('account')['role'] = RoleData.USER.value.get('id')
        serializer = RegisterUserSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return AccountService.login_with_username_password(user_data['account']['username'],
                                                               user_data['account']['password'])
