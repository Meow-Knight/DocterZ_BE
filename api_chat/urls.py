from rest_framework import routers

from api_chat.views import ChatViewSet

app_name = 'api_blog'
router = routers.SimpleRouter(trailing_slash=True)

router.register(r'', ChatViewSet, basename='chat')

urlpatterns = router.urls
