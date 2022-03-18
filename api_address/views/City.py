from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_address.serializers import CitySerializer
from api_address.models import City
from api_base.views import BaseViewSet


class CityViewSet(BaseViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = AdminPermission
    permission_map = {
        "get_all": []
    }

    @action(detail=False, methods=['get'])
    def get_all(self, request, *args, **kwargs):
        return Response(self.get_serializer(self.get_queryset(), many=True).data, status=status.HTTP_200_OK)
