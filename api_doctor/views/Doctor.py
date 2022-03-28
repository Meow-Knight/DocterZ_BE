from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from api_account.permissions import DoctorPermission, AdminPermission, DoctorOrAdminPermission
from api_base.views import BaseViewSet
from api_doctor.models.Doctor import Doctor
from api_doctor.serializers import DoctorSerializer
from api_doctor.services import DoctorService


class DoctorViewSet(BaseViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = []
    permission_map = {
        "signup": [AdminPermission],
        "login": [],
        "edit_own_profile": [DoctorPermission],
    }

    @action(detail=False, methods=['post'], url_path='signup')
    def signup(self, request, *args, **kwargs):
        response_data = DoctorService.signup(request)
        res_data = {"message": "Đăng ký thành công", "data": response_data}
        return Response(res_data, status=status.HTTP_201_CREATED)

    @action(methods=['put'], detail=False)
    def edit_own_profile(self, request, *args, **kwargs):
        data = request.data
        acc = request.user
        doctor = Doctor.objects.filter(account=acc)
        if doctor.exists():
            doctor = doctor.first()
            serializer = self.get_serializer(doctor, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
