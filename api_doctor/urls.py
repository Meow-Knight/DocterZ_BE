from rest_framework import routers

from api_doctor.views import DoctorViewSet, DepartmentViewSet, HospitalViewSet, ClinicViewSet

app_name = 'api_doctor'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'', DoctorViewSet, basename='doctor')
router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'hospital', HospitalViewSet, basename='hospital')
router.register(r'clinic', ClinicViewSet, basename='clinic')

urlpatterns = router.urls
