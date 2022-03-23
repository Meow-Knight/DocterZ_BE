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
    }
