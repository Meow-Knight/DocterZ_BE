from rest_framework import serializers

from api_doctor.models import Review
from api_user.serializers import ReviewerSerializer


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ShowReviewByDoctorSerializer(serializers.ModelSerializer):
    user = ReviewerSerializer()

    class Meta:
        model = Review
        fields = ['id', 'rate', 'comment', 'user']
