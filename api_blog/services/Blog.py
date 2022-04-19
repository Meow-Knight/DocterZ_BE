import os

from django.db import transaction
from django.db.models.functions import Collate

from api_base.services import CloudinaryService
from api_blog.models import Blog
from api_blog.serializers import BlogSerializer, BlogDetailSerializer
from api_doctor.models import Doctor
from django.db.models import Q, Value


class BlogService:
    @classmethod
    def upload_image(cls, image):
        upload_data = CloudinaryService.upload_image(image, os.getenv('CLOUDINARY_AVATAR_USER_FOLDER'))
        return upload_data.get("url")

    @classmethod
    def delete_image(cls, image):
        return CloudinaryService.delete_image(image, os.getenv('CLOUDINARY_AVATAR_USER_FOLDER'))

    @classmethod
    @transaction.atomic
    def create(cls, request):
        acc = request.user
        doctor = Doctor.objects.filter(account=acc)
        request.data._mutable = True
        if doctor.exists():
            doctor = doctor.first()
            request.data['doctor'] = doctor.pk
        if request.data.get('status') is None:
            request.data['status'] = True
        if request.data.get('image') is not None:
            request.data['image'] = cls.upload_image(request.data.get('image'))
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()
        blog = BlogDetailSerializer(serializer)
        return blog.data

    @classmethod
    @transaction.atomic
    def update(cls, request, kwargs):
        acc = request.user
        id_blog = kwargs.get('pk')
        request.data_mutable = True
        doctor = Doctor.objects.filter(account=acc)
        if doctor.exists():
            doctor = doctor.first()
        blog = Blog.objects.filter(doctor=doctor.pk, pk=id_blog)
        if blog.exists():
            blog = blog.first()
        if request.data.get('image') is not None:
            request.data['image'] = cls.upload_image(request.data.get('image'))
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer = serializer.save()
        blog = BlogDetailSerializer(serializer)
        return blog.data

    @classmethod
    @transaction.atomic
    def search(cls, request):
        search_query = request.query_params.get("q", "")
        search_query = Collate(Value(search_query), "utf8_general_ci")
        search_status = request.query_params.get("status", "true").title()
        query_set = Blog.objects.filter(Q(status=search_status),
                                        Q(title__icontains=search_query)
                                        | Q(desc__icontains=search_query)
                                        | Q(content__icontains=search_query))
        return query_set
