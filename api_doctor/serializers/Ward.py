from rest_framework import serializers

from api_doctor.models.District import District
from api_doctor.models.Ward import Ward
from api_doctor.serializers.District import DistrictSerializer


class FullAddressSerializer(serializers.ModelSerializer):
    district = DistrictSerializer()

    def to_representation(self, instance):
        data = super(FullAddressSerializer, self).to_representation(instance)
        res_data = dict()
        res_data['ward'] = {
            "id": data['id'],
            "code": data['code'],
            "name": data['name']
        }
        res_data['district'] = {
            "id": data['district']['id'],
            "code": data['district']['code'],
            "name": data['district']['name']
        }
        res_data['city'] = {
            "id": data['district']['city']['id'],
            "code": data['district']['city']['code'],
            "name": data['district']['city']['name']
        }
        return res_data

    class Meta:
        model = Ward
        fields = ('id', 'code', 'name', 'district')
