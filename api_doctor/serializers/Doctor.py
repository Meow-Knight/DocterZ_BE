from django.db import transaction
from rest_framework import serializers

from api_account.serializers import AccountSerializer, GeneralInfoAccountSerializer
from api_account.services import AccountService
from api_address.serializers import FullAddressSerializer, DeepWardSerializer
from api_doctor.models.Doctor import Doctor
from api_doctor.serializers import ClinicSerializer, ClinicCUDSerializer
from api_doctor.serializers.Hospital import HospitalSerializer


class DoctorSerializer(serializers.ModelSerializer):
    ward = DeepWardSerializer()
    address = FullAddressSerializer(required=False, source="ward")
    hospital = HospitalSerializer(required=False)
    clinic = ClinicSerializer(required=False)

    class Meta:
        model = Doctor
        fields = '__all__'
        depth = 1


class ListDoctorSerializer(serializers.ModelSerializer):
    full_address = serializers.SerializerMethodField()
    hospital_name = serializers.CharField(source='hospital.name')
    department_name = serializers.CharField(source='department.name')
    clinic_name = serializers.CharField(source='clinic.name')
    username = serializers.CharField(source='account.username')
    is_activate = serializers.BooleanField(source='account.is_activate')
    avatar = serializers.CharField(source='account.avatar')

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'phone',  'gender', 'email', 'birthday', 'full_address', 'hospital_name', 'department_name',
                  'clinic_name', 'graduation_year', 'username', 'is_activate', 'avatar']

    def get_full_address(self, instance):
        res = ""
        if instance.detail_address:
            res = instance.detail_address
        if instance.ward:
            res = res + instance.ward.get_full_address()
        return res


class RegisterDoctorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
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
            if clinic_data.get('ward') is not None:
                clinic_data['ward'] = clinic_data.get('ward').pk
            if instance.clinic:
                clinic = ClinicCUDSerializer(instance.clinic, data=clinic_data, partial=True)
                if clinic.is_valid(raise_exception=True):
                    validated_data['clinic'] = clinic.save()
            else:
                clinic = ClinicCUDSerializer(data=clinic_data)
                if clinic.is_valid(raise_exception=True):
                    validated_data['clinic'] = clinic.save()
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


class EditOwnDoctorProfileSerializer(EditDoctorProfileSerializer):
    class Meta:
        model = Doctor
        fields = ['full_name', 'gender', 'phone', 'email', 'birthday', 'graduation_year']


class AdminEditDoctorSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=30, source="account.username")

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'email', 'gender', 'graduation_year', 'detail_address', 'ward', 'hospital',
                  'department', 'clinic', 'username']
        
    def update(self, instance, validated_data):
        username = validated_data.pop('account').get('username')
        if username:
            instance.account.username = username
            instance.account.save()
        return super().update(instance, validated_data)


class GeneralInfoDoctorSerializer(serializers.ModelSerializer):
    account = GeneralInfoAccountSerializer()
    full_address = serializers.SerializerMethodField()
    hospital_name = serializers.CharField(source='hospital.name')
    department_name = serializers.CharField(source='department.name')
    clinic_name = serializers.CharField(source='clinic.name')
    username = serializers.CharField(source='account.username')
    is_activate = serializers.BooleanField(source='account.is_activate')
    avatar = serializers.CharField(source='account.avatar')

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'phone', 'gender', 'email', 'birthday', 'full_address', 'hospital_name',
                  'department_name',
                  'clinic_name', 'graduation_year', 'username', 'is_activate', 'avatar', 'account']


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
