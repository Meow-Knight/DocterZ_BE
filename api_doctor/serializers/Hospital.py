from rest_framework import serializers

from api_doctor.models.Hospital import Hospital
from api_address.serializers import FullAddressSerializer


class HospitalSerializer(serializers.ModelSerializer):
    address = FullAddressSerializer()

    class Meta:
        model = Hospital
        fields = '__all__'
        depth = 1
