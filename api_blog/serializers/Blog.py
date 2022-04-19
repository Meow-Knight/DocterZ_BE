from rest_framework import serializers

from api_blog.models import Blog
from api_doctor.models import Doctor
from api_doctor.serializers import ItemDoctorSerializer


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'


class BlogDetailSerializer(serializers.ModelSerializer):
    doctor = ItemDoctorSerializer()

    class Meta:
        model = Blog
        fields = ["id", "content", "doctor", "status", "title", "desc",
                  "created_at", "updated_at", "image", ]
