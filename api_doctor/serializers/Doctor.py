from rest_framework import serializers

from api_account.serializers import AccountSerializer
from api_account.services import AccountService
from api_doctor.models import Clinic
from api_doctor.models.Department import Department
from api_doctor.models.Doctor import Doctor
from api_doctor.serializers import ClinicSerializer
from api_doctor.serializers.Hospital import HospitalSerializer
from api_doctor.serializers.Ward import FullAddressSerializer


class DoctorSerializer(serializers.ModelSerializer):
    address = FullAddressSerializer()
    hospital = HospitalSerializer()
    clinic = ClinicSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'
        depth = 1


class RegisterDoctorSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    def create(self, validated_data):
        account_data = validated_data.pop("account")
        if validated_data.get("email") is not None:
            account_data["email"] = validated_data.get("email")
        account = AccountService.create_account(account_data)
        validated_data['account'] = account
        return super().create(validated_data)

    class Meta:
        model = Doctor
        fields = '__all__'
