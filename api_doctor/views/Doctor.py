from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from api_account.permissions import DoctorPermission, AdminPermission, DoctorOrAdminPermission
from api_base.views import BaseViewSet
from api_doctor.models.Doctor import Doctor
from api_doctor.serializers import DoctorSerializer, ItemDoctorSerializer, EditDoctorProfileSerializer, \
    ListDoctorSerializer, AdminEditDoctorSerializer
from api_doctor.services import DoctorService


class DoctorViewSet(BaseViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = []
    permission_map = {
        "signup": [AdminPermission],
        "edit_own_profile": [DoctorPermission],
        "search": [],
        "get_all": [AdminPermission],
        "update": [AdminPermission],
        "deactivate": [AdminPermission],
        "activate": [AdminPermission],
    }
    serializer_map = {
        "list": ListDoctorSerializer,
        "search": ItemDoctorSerializer,
        "edit_own_profile": EditDoctorProfileSerializer,
        "get_all": ListDoctorSerializer,
        "update": AdminEditDoctorSerializer
    }

    def create(self, request, *args, **kwargs):
        response_data = DoctorService.signup(request)
        return Response(response_data, status=status.HTTP_201_CREATED)

    @action(methods=['put'], detail=False)
    def edit_own_profile(self, request, *args, **kwargs):
        data = request.data
        acc = request.user
        doctor = Doctor.objects.filter(account=acc)
        if doctor.exists():
            doctor = doctor.first()
            serializer = self.get_serializer(doctor, data=data, partial=True)
            if serializer.is_valid(raise_exception=True):
                doctor = serializer.save()
                res_data = DoctorSerializer(doctor)
                return Response(res_data.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def search(self, request, *args, **kwargs):
        query_set = DoctorService.search(request)
        self.queryset = query_set
        return super().list(request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def get_all(self, request, *args, **kwargs):
        return Response(self.get_serializer(self.queryset, many=True).data)
