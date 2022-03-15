from django.contrib.auth.models import UserManager
from django.db import models

from api_base.models import TimeStampedModel


class City(TimeStampedModel):
    objects = UserManager()
    code = models.IntegerField()
    name = models.CharField(max_length=500, null=False, unique=True)

    class Meta:
        db_table = "city"
        ordering = ('created_at',)
