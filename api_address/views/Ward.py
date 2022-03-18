from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_address.serializers import WardSerializer
from api_address.models import District, Ward
from api_base.views import BaseViewSet


class WardViewSet(BaseViewSet):
    queryset = Ward.objects.all()
    serializer_class = WardSerializer
    permission_classes = AdminPermission
    permission_map = {
        "get_by_district_id": []
    }

    @action(detail=False, methods=['get'])
    def get_by_district_id(self, request, *args, **kwargs):
        district_id = request.query_params.get('district_id', None)
        if not district_id or not District.objects.filter(code=district_id).exists():
            return Response({"details": "Invalid city_id param in request url"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.get_serializer(Ward.objects.filter(district_id=district_id), many=True).data,
                        status=status.HTTP_200_OK)
