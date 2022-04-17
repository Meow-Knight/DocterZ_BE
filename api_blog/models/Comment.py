from django.contrib.auth.models import UserManager
from django.db import models
from api_base.models import TimeStampedModel
from api_blog.models import Blog
from api_user.models import User


class Comment(TimeStampedModel):
    objects = UserManager()
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="blog")
    blog = models.ForeignKey(Blog, null=True, on_delete=models.SET_NULL, related_name="blog")
    content = models.TextField(null=False)
    status = models.BooleanField(default=True)
    rate = models.FloatField(null=True)

    class Meta:
        db_table = "comment"
        ordering = ('created_at',)
