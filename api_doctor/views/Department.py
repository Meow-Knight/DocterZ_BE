from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Department
from api_doctor.serializers import DepartmentSerializer


class DepartmentViewSet(BaseViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AdminPermission]
    permission_map = {
        "list": [],
        "retrieve": [],
        "get_all": []
    }

    @action(detail=False, methods=['get'])
    def get_all(self, request, *args, **kwargs):
        return Response(DepartmentSerializer(Department.objects.all().order_by('name'), many=True).data)
