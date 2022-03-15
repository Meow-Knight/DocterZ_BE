from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from api_account.permissions import DoctorPermission, AdminPermission
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
    }

    @action(detail=False, methods=['post'], url_path='signup')
    def signup(self, request, *args, **kwargs):
        response_data = DoctorService.signup(request)
        res_data = {"message": "Register Successfully", "profile": response_data}
        return Response(res_data, status=status.HTTP_201_CREATED)

