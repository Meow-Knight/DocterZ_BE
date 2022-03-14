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
    account = AccountSerializer()
    insurance = InsuranceSerializer()

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        account_data = validated_data.pop("account")
        insurance_data = validated_data.pop("insurance")
        account = AccountService.create_account(account_data)
        Insurance.objects.create(**insurance_data)
        validated_data['account'] = account
        return super().create(validated_data)
