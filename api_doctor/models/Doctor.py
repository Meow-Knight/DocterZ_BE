from django.contrib.auth.models import UserManager
from django.db import models

from api_account.models import Account
from api_base.models import TimeStampedModel
from api_doctor.models import Clinic
from api_doctor.models import Department
from api_doctor.models import Hospital
from api_address.models import Ward


class Doctor(TimeStampedModel):
    objects = UserManager()
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    detail_address = models.CharField(max_length=200, null=True, blank=True)
    ward = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True, related_name="doctor")
    hospital = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True, related_name="doctor")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name="doctor")
    clinic = models.ForeignKey(Clinic, on_delete=models.SET_NULL, null=True, related_name="doctor")
    year_of_starting_work = models.IntegerField(null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        db_table = "doctor"
        ordering = ('created_at',)
