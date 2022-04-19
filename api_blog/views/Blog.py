from rest_framework import status
from rest_framework.response import Response
from api_account.permissions import DoctorPermission, DoctorOrAdminPermission
from api_base.views import BaseViewSet
from api_blog.models import Blog
from api_blog.serializers import BlogSerializer, BlogDetailSerializer
from api_blog.services import BlogService


class BlogViewSet(BaseViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [DoctorPermission]
    permission_map = {
        "list": [],
        "retrieve": [],
    }
    serializer_map = {
        "retrieve": BlogDetailSerializer,
        "list": BlogDetailSerializer
    }

    def create(self, request, *args, **kwargs):
        res = BlogService.create(request)
        return Response(res, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        query_set = BlogService.search(request)
        self.queryset = query_set
        self.serializer_class = BlogSerializer
        return super().list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        res = BlogService.update(request, kwargs)
        return Response(res, status=status.HTTP_200_OK)

