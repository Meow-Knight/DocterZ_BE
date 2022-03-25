from django.db import transaction
from rest_framework import serializers

from api_account.models import Account
from api_account.serializers import AccountSerializer
from api_account.services import AccountService
from api_doctor.models import Clinic
from api_doctor.models.Doctor import Doctor
from api_doctor.serializers import ClinicSerializer, ClinicCUDSerializer
from api_doctor.serializers.Hospital import HospitalSerializer
from api_address.serializers import FullAddressSerializer


class DoctorSerializer(serializers.ModelSerializer):
    ward = FullAddressSerializer(required=False)
    hospital = HospitalSerializer(required=False)
    clinic = ClinicSerializer(required=False)
    avatar = serializers.ImageField(required=False)

    @transaction.atomic
    def update(self, instance, validated_data):
        clinic_data = validated_data.get('clinic')
        avatar_data = validated_data.get('avatar')
        if clinic_data is not None:
            validated_data.pop('clinic')
            clinic = ClinicCUDSerializer(instance.clinic, data=clinic_data, partial=True)
            if clinic.is_valid(raise_exception=True):
                clinic.save()
        if avatar_data is not None:
            validated_data.pop('avatar')
            account = instance.account
            AccountService.delete_avatar(account.avatar)
            avatar_link = AccountService.upload_avatar(avatar_data)
            account.avatar = avatar_link
            account.save()
        return super().update(instance, validated_data)

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
