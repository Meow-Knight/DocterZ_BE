from rest_framework import serializers

from api_doctor.models.District import District
from api_doctor.serializers.City import CitySerializer


class DistrictSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = District
        fields = ('id', 'code', 'name', 'city')
