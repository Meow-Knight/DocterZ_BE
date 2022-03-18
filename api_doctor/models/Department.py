from django.contrib.auth.models import UserManager
from django.db import models

from api_base.models import TimeStampedModel


class Department(TimeStampedModel):
    objects = UserManager()
    name = models.CharField(max_length=50, null=False, unique=True)

    class Meta:
        db_table = "department"
        ordering = ('created_at',)
