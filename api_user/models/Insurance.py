from django.db import models

from api_base.models import TimeStampedModel


class Insurance(TimeStampedModel):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    expired_date = models.DateField()
    created_date = models.DateField()

    class Meta:
        db_table = "insurance"
        ordering = ('created_at',)
