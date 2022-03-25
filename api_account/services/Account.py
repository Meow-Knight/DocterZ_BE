import os

from django.contrib.auth.hashers import make_password, check_password
from dotenv import load_dotenv
from rest_framework_simplejwt.tokens import RefreshToken

from api_account.models import Account
from api_base.services import CloudinaryService

load_dotenv()


class AccountService:

    @classmethod
    def is_valid_login_data(cls, user_data):
        username = user_data.get("username", '')
        password = user_data.get("password", '')

        if not username or not password:
            return False

        user_queryset = Account.objects.filter(username=username)
        if not user_queryset.exists():
            return False

        user = user_queryset.first()
        is_correct_password = check_password(password, user.password)
        if not is_correct_password:
            return False
        return True

    @classmethod
    def login_with_username_password(cls, username, password):
        account = Account.objects.filter(username=username)
        if account.exists():
            account = account.first()
            if check_password(password, account.password):
                token = RefreshToken.for_user(account)
                return {'id': account.id,
                        'role': account.role.name,
                        'access_token': str(token.access_token),
                        'refresh_token': str(token)}
        return None

    @classmethod
    def create_account(cls, account_data):
        password = account_data.get("password")
        if not password:
            return None
        account_data['password'] = make_password(password)
        return Account.objects.create(**account_data)

    @classmethod
    def upload_avatar(cls, image):
        upload_data = CloudinaryService.upload_image(image, os.getenv('CLOUDINARY_AVATAR_USER_FOLDER'))
        return upload_data.get("url")

    @classmethod
    def delete_avatar(cls, image):
        return CloudinaryService.delete_image(image, os.getenv('CLOUDINARY_AVATAR_USER_FOLDER'))
