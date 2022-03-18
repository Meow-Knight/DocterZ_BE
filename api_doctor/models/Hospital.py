from django.contrib.auth.models import UserManager
from django.db import models

from api_base.models import TimeStampedModel
from api_address.models.Ward import Ward


class Hospital(TimeStampedModel):
    objects = UserManager()
    name = models.CharField(max_length=50, null=False, unique=True)
    detail_address = models.CharField(max_length=200, null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, related_name="hospital")

    class Meta:
        db_table = "hospital"
        ordering = ('created_at',)
