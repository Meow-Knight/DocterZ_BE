from rest_framework import serializers

from api_doctor.models.City import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name', 'code')
