from django.db import transaction
from rest_framework.exceptions import ValidationError

from api_account.constants import RoleData
from api_account.services import AccountService
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
            serializer.save()
            return AccountService.login_with_username_password(user_data['account']['username'],
                                                               user_data['account']['password'])
