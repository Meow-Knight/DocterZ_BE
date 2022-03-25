from rest_framework import serializers

from api_user.models import Insurance


class InsuranceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Insurance
        fields = ['code', 'name', 'expired_date', 'created_date']
