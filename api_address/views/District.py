from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_address.serializers import DistrictSerializer
from api_address.models import District, City
from api_base.views import BaseViewSet


class DistrictViewSet(BaseViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = []
    permission_map = {
        "get_by_city_id": []
    }

    @action(detail=False, methods=['get'])
    def get_by_city_id(self, request, *args, **kwargs):
        city_id = request.query_params.get('city_id', None)
        if not city_id or not City.objects.filter(code=city_id).exists():
            return Response({"details": "Invalid city_id param in request url"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.get_serializer(District.objects.filter(city_id=city_id), many=True).data,
                        status=status.HTTP_200_OK)
