from rest_framework import routers

from api_blog.views import BlogViewSet

app_name = 'api_blog'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'', BlogViewSet, basename='blog')

urlpatterns = router.urls
