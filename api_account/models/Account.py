from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

from api_account.models import Role
from api_base.models import TimeStampedModel


class Account(AbstractBaseUser, TimeStampedModel):
    objects = UserManager()
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200, null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "account"
        ordering = ('created_at',)
