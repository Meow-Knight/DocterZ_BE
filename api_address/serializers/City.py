from rest_framework import serializers

from api_address.models.City import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'
