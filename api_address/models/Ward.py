from django.db import models

from api_address.models import District


class Ward(models.Model):
    objects = models.Manager
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='wards')

    class Meta:
        db_table = "ward"
        ordering = ('name',)

    def get_full_address(self):
        full_detail_address = [self.name, self.district.name, self.district.city.name]
        return ", ".join(full_detail_address)
