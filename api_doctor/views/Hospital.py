from rest_framework import status
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Hospital
from api_doctor.serializers import HospitalSerializer, HospitalCUDSerializer


class HospitalViewSet(BaseViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [AdminPermission]
    permission_map = {
        "list": [],
        "retrieve": [],
    }
    serializer_map = {
        "create": HospitalCUDSerializer,
        "update": HospitalCUDSerializer,
        "destroy": HospitalCUDSerializer
    }

