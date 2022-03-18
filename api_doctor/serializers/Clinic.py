from rest_framework import serializers

from api_doctor.models import Clinic
from api_address.serializers import FullAddressSerializer


class ClinicSerializer(serializers.ModelSerializer):
    address = FullAddressSerializer()

    class Meta:
        model = Clinic
        fields = '__all__'


class ClinicRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = '__all__'
