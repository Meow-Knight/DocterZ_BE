from django.contrib.auth.models import UserManager
from django.db import models

from api_base.models import TimeStampedModel
from api_doctor.models.District import District


class Ward(TimeStampedModel):
    objects = UserManager()
    code = models.IntegerField()
    name = models.CharField(max_length=500, null=False, unique=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT, related_name="ward")

    class Meta:
        db_table = "ward"
        ordering = ('created_at',)
