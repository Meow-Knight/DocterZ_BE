from django.contrib.auth.models import UserManager
from django.db import models

from api_account.models import Account
from api_base.models import TimeStampedModel
from api_doctor.models.Clinic import Clinic
from api_doctor.models.Department import Department
from api_doctor.models.Hospital import Hospital
from api_doctor.models.Ward import Ward


class Doctor(TimeStampedModel):
    objects = UserManager()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    address = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, related_name="doctor")
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, related_name="doctor")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="doctor")
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, related_name="doctor")
    joined_date = models.DateField(null=True, blank=True)
    certificate = models.CharField(max_length=200, null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"
        ordering = ('created_at',)
