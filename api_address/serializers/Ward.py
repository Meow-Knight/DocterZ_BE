from rest_framework import serializers

from api_address.models.Ward import Ward
from api_address.serializers.District import DistrictSerializer


class WardSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    class Meta:
        model = Ward
        fields = '__all__'


class FullAddressSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    def to_representation(self, instance):
        data = super(FullAddressSerializer, self).to_representation(instance)
        res_data = dict()
        res_data['ward'] = {
            "code": data['code'],
            "name": data['name']
        }
        res_data['district'] = {
            "code": data['district']['code'],
            "name": data['district']['name']
        }
        res_data['city'] = {
            "code": data['district']['city']['code'],
            "name": data['district']['city']['name']
        }
        return res_data

    class Meta:
        model = Ward
        fields = '__all__'
