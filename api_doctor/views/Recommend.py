from django.db.models import Case, When
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import UserPermission, AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Review
from api_doctor.serializers import ReviewSerializer
from api_doctor.services import RecommendService


class RecommendViewSet(BaseViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = []

    def list(self, request, *args, **kwargs):
        res = RecommendService.recommend(request)
        return Response(res, status=status.HTTP_200_OK)
