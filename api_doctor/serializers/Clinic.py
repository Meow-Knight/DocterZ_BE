from rest_framework import serializers

from api_doctor.models import Clinic
from api_address.serializers import FullAddressSerializer


class ClinicSerializer(serializers.ModelSerializer):
    ward = FullAddressSerializer(required=False)

    class Meta:
        model = Clinic
        fields = '__all__'


class ClinicCUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clinic
        fields = '__all__'
