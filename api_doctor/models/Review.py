from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from api_base.models import TimeStampedModel
from api_doctor.models import Doctor
from api_user.models import User


class Review(TimeStampedModel):
    rate = models.IntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="reviews")

    class Meta:
        db_table = "review"
        ordering = ('-created_at',)
        unique_together = ('user', 'doctor',)
