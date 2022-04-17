from rest_framework import serializers

from api_blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "content", "doctor", "status"]
