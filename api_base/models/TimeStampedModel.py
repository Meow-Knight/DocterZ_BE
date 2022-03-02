import uuid

from django.utils import timezone
from djongo import models


class TimeStampedModel(models.Model):
    objects = models.DjongoManager()
    id = models.ObjectIdField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
