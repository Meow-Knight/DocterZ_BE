from django.db import transaction

from api_blog.models import Blog
from api_blog.serializers import BlogSerializer
from api_doctor.models import Doctor


class BlogService:
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
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data

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
        serializer = BlogSerializer(blog, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return serializer.data
