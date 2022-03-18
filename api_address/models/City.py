from django.db import models


class City(models.Model):
    objects = models.Manager
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "city"
        ordering = ('name',)
