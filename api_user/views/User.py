import json

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import UserPermission, AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Doctor
from api_doctor.serializers import DoctorSerializer
from api_user.models import User
from api_user.serializers.User import RegisterUserSerializer, EditUserSerializer, ListUserSerializer
from api_user.services import UserService


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [UserPermission]
    permission_map = {
        "login": [],
        "signup": [],
        "list": [AdminPermission],
    }
    serializer_map = {
        "edit_own_profile": EditUserSerializer,
        "detail_doctor": DoctorSerializer,
        "list": ListUserSerializer
    }

    @action(detail=False, methods=['post'])
    def signup(self, request, *args, **kwargs):
        response_data = UserService.signup(request)
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['put'])
    def edit_own_profile(self, request, *args, **kwargs):
        account = request.user
        user = User.objects.get(account=account)

        request_data = request.data.dict()

        insurance_data = request_data.get('insurance')
        if insurance_data:
            insurance_data = json.loads(insurance_data)
            request_data['insurance'] = insurance_data
        serializer = self.get_serializer(user, data=request_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            response_data = serializer.data
            response_data['avatar'] = user.account.avatar
            return Response(response_data)

    @action(methods=['get'], detail=False)
    def detail_doctor(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctor_id')
        doctor = Doctor.objects.filter(pk=doctor_id)
        if doctor.exists():
            doctor = DoctorSerializer(doctor.first())
            return Response(doctor.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "doctor id không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)
