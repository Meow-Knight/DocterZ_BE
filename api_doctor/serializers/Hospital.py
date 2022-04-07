from rest_framework import serializers

from api_doctor.models.Hospital import Hospital
from api_address.serializers import FullAddressSerializer


class HospitalSerializer(serializers.ModelSerializer):
    ward = FullAddressSerializer()

    def to_representation(self, instance):
        data = super(HospitalSerializer, self).to_representation(instance)
        data['address'] = data.pop('ward')
        return data

    class Meta:
        model = Hospital
        fields = '__all__'
        depth = 1


class HospitalCUDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = '__all__'


class HospitalWithNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hospital
        fields = ['id', 'name']
