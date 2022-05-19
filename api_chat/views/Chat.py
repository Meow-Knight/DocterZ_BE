from rest_framework.permissions import IsAuthenticated

from api_base.views import BaseViewSet
from api_chat.models import Chat
from api_chat.serializers import ChatSerializer


class ChatViewSet(BaseViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated]
    permission_map = {
    }
    serializer_map = {
    }

    def create(self, request, *args, **kwargs):
        request.data['sender'] = request.user
        return super().create(request, *args, **kwargs)

    # def