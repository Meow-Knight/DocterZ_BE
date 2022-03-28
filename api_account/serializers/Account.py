from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from api_account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.get('password')
        password = make_password(password)
        validated_data['password'] = password
        return super().create(validated_data)


class UpdateGeneralAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'avatar']


class GeneralInfoAccountSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='role.name')

    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'avatar', 'role', 'is_active']
