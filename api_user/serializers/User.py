from rest_framework import serializers

from api_account.serializers import AccountSerializer
from api_account.services import AccountService
from api_user.models import User, Insurance
from api_user.serializers import InsuranceSerializer


class FullUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class RegisterUserSerializer(serializers.ModelSerializer):
    insurance = InsuranceSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        insurance_data = validated_data.pop("insurance")
        insurance = Insurance.objects.create(**insurance_data)
        validated_data['insurance'] = insurance
        return super().create(validated_data)
