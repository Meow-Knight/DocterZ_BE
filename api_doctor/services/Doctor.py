from django.db import transaction
from django.db.models import Value, Q
from django.db.models.functions import Collate

from api_account.constants import RoleData
from api_account.services import AccountService
from api_doctor.models import Doctor
from api_doctor.serializers import ClinicCUDSerializer
from api_doctor.serializers.Doctor import RegisterDoctorSerializer


class DoctorService:
    @classmethod
    @transaction.atomic
    def signup(cls, request):
        user_data = request.data
        if user_data.get('account') is not None:
            user_data.get('account')['role'] = RoleData.DOCTOR.value.get('id')
        if user_data.get('clinic') is not None:
            clinic_serializer = ClinicCUDSerializer(data=user_data.get('clinic'))
            if clinic_serializer.is_valid(raise_exception=True):
                user_data['clinic'] = clinic_serializer.save().pk
        serializer = RegisterDoctorSerializer(data=user_data)
        if serializer.is_valid(raise_exception=True):
            doctor = serializer.save()
            return AccountService.get_login_info(doctor.account)

    @classmethod
    def search(cls, request):
        keyword = request.query_params.get('q', '')
        utf8_keyword = Collate(Value(keyword), "utf8_general_ci")
        return Doctor.objects.filter(Q(full_name__icontains=utf8_keyword)
                                        | Q(hospital__name__icontains=utf8_keyword)
                                        | Q(department__name__icontains=utf8_keyword)
                                        | Q(clinic__name__icontains=utf8_keyword))
