from rest_framework import routers

from api_doctor.views import DoctorViewSet

app_name = 'api_doctor'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'', DoctorViewSet, basename='doctor')

urlpatterns = router.urls
