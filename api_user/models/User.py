from django.contrib.auth.models import UserManager
from django.db import models

from api_account.models import Account
from api_base.models import TimeStampedModel
from api_user.models import Insurance


class User(TimeStampedModel):
    objects = UserManager()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    career = models.CharField(max_length=20, null=True, blank=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.SET_NULL, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "user"
        ordering = ('created_at',)
