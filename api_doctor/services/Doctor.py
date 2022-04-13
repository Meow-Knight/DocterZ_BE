from django.db import transaction
from django.db.models import Value, Q
from django.db.models.functions import Collate

from api_account.constants import RoleData
from api_account.serializers import AccountSerializer
from api_account.services import AccountService
from api_doctor.models import Doctor
from api_doctor.serializers.Doctor import RegisterDoctorSerializer

from dotenv import load_dotenv
import os

load_dotenv()


class DoctorService:
    @classmethod
    @transaction.atomic
    def signup(cls, request):
        doctor_data = request.data
        doctor_data['role'] = RoleData.DOCTOR.value.get('id')
        doctor_data['password'] = os.getenv('DEFAULT_DOCTOR_PASSWORD')
        account_serializer = AccountSerializer(data=doctor_data)
        if account_serializer.is_valid(raise_exception=True):
            account = account_serializer.save()
            doctor_data['account'] = account.id.hex
            doctor_serializer = RegisterDoctorSerializer(data=doctor_data)
            if doctor_serializer.is_valid(raise_exception=True):
                doctor = doctor_serializer.save()
                return AccountService.get_login_info(doctor.account)

    @classmethod
    def search(cls, request):
        keyword = request.query_params.get('q', '')
        utf8_keyword = Collate(Value(keyword), "utf8_general_ci")
        return Doctor.objects.filter(Q(full_name__icontains=utf8_keyword)
                                        | Q(hospital__name__icontains=utf8_keyword)
                                        | Q(department__name__icontains=utf8_keyword)
                                        | Q(clinic__name__icontains=utf8_keyword))
