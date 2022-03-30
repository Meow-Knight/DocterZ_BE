from django.db import transaction
from rest_framework import serializers

from api_account.serializers import AccountSerializer, GeneralInfoAccountSerializer
from api_account.services import AccountService
from api_address.serializers import FullAddressSerializer
from api_doctor.models.Doctor import Doctor
from api_doctor.serializers import ClinicSerializer, ClinicCUDSerializer
from api_doctor.serializers.Hospital import HospitalSerializer


class DoctorSerializer(serializers.ModelSerializer):
    ward = FullAddressSerializer(required=False)
    hospital = HospitalSerializer(required=False)
    clinic = ClinicSerializer(required=False)

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


class EditDoctorProfileSerializer(serializers.ModelSerializer):
    clinic = ClinicCUDSerializer(required=False)
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


class GeneralInfoDoctorSerializer(serializers.ModelSerializer):
    account = GeneralInfoAccountSerializer()

    class Meta:
        model = Doctor
        fields = '__all__'


class ItemDoctorSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()
    hospital_name = serializers.CharField(source='hospital.name')
    department_name = serializers.CharField(source='department.name')
    clinic_name = serializers.CharField(source='clinic.name')

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'gender', 'email', 'address', 'hospital_name', 'department_name', 'clinic_name']

    def get_address(self, instance):
        res = ""
        if instance.detail_address:
            res = instance.detail_address
        if instance.ward:
            res = res + instance.ward.get_full_address()
        return res
