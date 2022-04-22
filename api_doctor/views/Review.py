from django.db.models import Case, When
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import UserPermission, AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Review
from api_doctor.serializers import ClinicWithNameSerializer, ReviewSerializer, ShowReviewByDoctorSerializer
from api_user.models import User


class ReviewViewSet(BaseViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [UserPermission]
    permission_map = {
        "list": [AdminPermission],
        "retrieve": [],
        "get_all": []
    }
    serializer_map = {
        "get_all": ClinicWithNameSerializer,
        "get_by_doctor_id": ShowReviewByDoctorSerializer
    }

    @action(detail=False, methods=['get'])
    def get_by_doctor_id(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctor_id')
        review_qs = Review.objects.filter(doctor_id=doctor_id)
        if not request.user.is_anonymous:
            user = User.objects.get(account=request.user)
            review_qs = review_qs.order_by(Case(When(user=user, then=0), default=1),
                                           '-updated_at')
        else:
            review_qs = review_qs.order_by('-updated_at')

        self.queryset = review_qs
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        account = request.user
        user = User.objects.get(account=account)
        request.data['user'] = user.id.hex
        return super().create(request)

    def update(self, request, *args, **kwargs):
        account = request.user
        user = User.objects.get(account=account)
        review = self.get_object()
        if review.user != user:
            return Response({"error_message": "Bạn không được phép chỉnh sửa đánh giá này"},
                            status=status.HTTP_400_BAD_REQUEST)

        request.data['user'] = user.id.hex
        return super().update(request)

    def partial_update(self, request, *args, **kwargs):
        return Response({"error_message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        account = request.user
        user = User.objects.get(account=account)
        review = self.get_object()
        if review.user != user:
            return Response({"error_message": "Bạn không được phép xóa đánh giá này"},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().destroy(request)
