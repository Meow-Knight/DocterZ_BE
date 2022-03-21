from rest_framework import serializers

from api_address.models.District import District
from api_address.serializers.City import CitySerializer


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = District
        fields = '__all__'
