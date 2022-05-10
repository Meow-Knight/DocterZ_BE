from rest_framework import routers

from api_doctor.views import DoctorViewSet, DepartmentViewSet, HospitalViewSet, ClinicViewSet, ReviewViewSet, \
    RecommendViewSet

app_name = 'api_doctor'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'department', DepartmentViewSet, basename='department')
router.register(r'hospital', HospitalViewSet, basename='hospital')
router.register(r'clinic', ClinicViewSet, basename='clinic')
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'recommend', RecommendViewSet, basename='recommend')
router.register(r'', DoctorViewSet, basename='doctor')

urlpatterns = router.urls
