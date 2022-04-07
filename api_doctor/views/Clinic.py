from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Clinic
from api_doctor.serializers import ClinicCUDSerializer, ClinicWithNameSerializer


class ClinicViewSet(BaseViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicCUDSerializer
    permission_classes = [AdminPermission]
    permission_map = {
        "list": [],
        "retrieve": [],
        "get_all": []
    }
    serializer_map = {
        "get_all": ClinicWithNameSerializer
    }

    @action(detail=False, methods=['get'])
    def get_all(self, request, *args, **kwargs):
        return Response(self.get_serializer(Clinic.objects.all().order_by('name'), many=True).data)
