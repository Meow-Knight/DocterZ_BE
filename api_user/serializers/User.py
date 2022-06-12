from django.db import transaction
from rest_framework import serializers

from api_account.serializers import GeneralInfoAccountSerializer
from api_account.services import AccountService
from api_user.models import User, Insurance
from api_user.serializers import InsuranceSerializer


class FullUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'name', 'phone', 'gender', 'birthday', 'career']


class GeneralInfoUserSerializer(serializers.ModelSerializer):
    account = GeneralInfoAccountSerializer()

    class Meta:
        model = User
        fields = '__all__'


class ReviewerSerializer(serializers.ModelSerializer):
    avatar = serializers.CharField(source='account.avatar')

    class Meta:
        model = User
        fields = ['id', 'name', 'avatar']


class RegisterUserSerializer(serializers.ModelSerializer):
    insurance = InsuranceSerializer(required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        insurance_data = validated_data.get("insurance")
        if insurance_data:
            insurance = Insurance.objects.create(**insurance_data)
            validated_data['insurance'] = insurance
        return super().create(validated_data)


class EditUserSerializer(serializers.ModelSerializer):
    insurance = InsuranceSerializer(required=False)
    avatar = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ('name', 'phone', 'birthday', 'gender', 'career', 'insurance', 'avatar')

    @transaction.atomic
    def update(self, instance, validated_data):
        insurance_data = validated_data.get('insurance')
        avatar = validated_data.get('avatar')
        if insurance_data:
            validated_data.pop('insurance')
            if not instance.insurance:
                insurance_serializer = InsuranceSerializer(data=insurance_data)
                if insurance_serializer.is_valid(raise_exception=True):
                    insurance = insurance_serializer.save()
                    validated_data['insurance'] = insurance
            else:
                insurance_serializer = InsuranceSerializer(instance.insurance, data=insurance_data, partial=True)
                if insurance_serializer.is_valid(raise_exception=True):
                    insurance_serializer.save()
        if avatar:
            validated_data.pop('avatar')
            account = instance.account
            AccountService.delete_avatar(account.avatar)
            avatar_link = AccountService.upload_avatar(avatar)
            account.avatar = avatar_link
            account.save()

        return super().update(instance, validated_data)
