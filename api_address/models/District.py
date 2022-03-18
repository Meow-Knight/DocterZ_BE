from django.db import models

from api_address.models import City


class District(models.Model):
    objects = models.Manager
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')

    class Meta:
        db_table = "district"
        ordering = ('name',)
