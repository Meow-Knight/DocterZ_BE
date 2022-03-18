from rest_framework import routers

from api_address.views import CityViewSet, DistrictViewSet, WardViewSet

app_name = 'api_address'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'city', CityViewSet, basename='city')
router.register(r'district', DistrictViewSet, basename='district')
router.register(r'ward', WardViewSet, basename='ward')

urlpatterns = router.urls
