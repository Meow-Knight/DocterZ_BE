from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class = None
    required_alternate_scopes = {}
    serializer_map = {}
    permission_map = {
        "deactivate": [AdminPermission],
        "activate": [AdminPermission]
    }

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)

    def get_permissions(self):
        return [permission() for permission in self.permission_map.get(self.action, self.permission_classes)]

    @action(detail=True, methods=['put'])
    def deactivate(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response({"detail": "deactivated"})

    @action(detail=True, methods=['put'])
    def activate(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = True
        instance.save()
        return Response({"detail": "activated"})
