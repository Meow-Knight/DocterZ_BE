from rest_framework import status

from rest_framework.decorators import action
from rest_framework.response import Response

from api_account.permissions import AdminPermission
from api_base.views import BaseViewSet
from api_doctor.models import Doctor
from api_user.models import User


class AdminViewSet(BaseViewSet):
    queryset = None
    serializer_class = None
    permission_classes = [AdminPermission]
    permission_map = {
    }

    @action(detail=False, methods=['put'])
    def deactivate_user(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        user = User.objects.filter(id=user_id)
        if user.exists():
            user = user.first()
            user.is_activate = False
            user.account.is_activate = False
            user.account.save()
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "user id không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def activate_user(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        user = User.objects.filter(id=user_id)
        if user.exists():
            user = user.first()
            user.is_activate = True
            user.account.is_activate = True
            user.account.save()
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "user id không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def deactivate_doctor(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctor_id')
        doctor = Doctor.objects.filter(id=doctor_id)
        if doctor.exists():
            doctor = doctor.first()
            doctor.is_activate = False
            doctor.account.is_activate = False
            doctor.account.save()
            doctor.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "doctor id không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'])
    def activate_doctor(self, request, *args, **kwargs):
        doctor_id = request.query_params.get('doctor_id')
        doctor = User.objects.filter(id=doctor_id)
        if doctor.exists():
            doctor = doctor.first()
            doctor.is_activate = True
            doctor.account.is_activate = True
            doctor.account.save()
            doctor.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "doctor id không hợp lệ"}, status=status.HTTP_400_BAD_REQUEST)
