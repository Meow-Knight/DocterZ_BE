from django.contrib.auth.models import UserManager
from django.db import models
from api_base.models import TimeStampedModel
from api_doctor.models import Doctor


class Blog(TimeStampedModel):
    objects = UserManager()
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL, related_name="blog")
    content = models.TextField(null=False)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "blog"
        ordering = ('created_at',)
