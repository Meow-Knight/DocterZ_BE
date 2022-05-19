from django.db import models

from api_account.models import Account
from api_base.models import TimeStampedModel


class Chat(TimeStampedModel):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="chats")
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="chats")
    content = models.TextField()

    class Meta:
        db_table = "chat"
        ordering = ('created_at',)
