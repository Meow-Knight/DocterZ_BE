from django.contrib.auth.models import UserManager
from django.db import models

from api_base.models import TimeStampedModel
from api_doctor.models.City import City


class District(TimeStampedModel):
    objects = UserManager()
    code = models.IntegerField()
    name = models.CharField(max_length=500, null=False, unique=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="district")

    class Meta:
        db_table = "district"
        ordering = ('created_at',)
