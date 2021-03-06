from django.db import migrations

import json


def initial_address(apps, schema_editor):

    city_model = apps.get_model("api_address", "City")
    district_model = apps.get_model("api_address", "District")
    ward_model = apps.get_model("api_address", "Ward")

    address_data = json.load(open('api_address/constants/address.json', encoding="utf8"))

    cities = []
    districts = []
    wards = []

    for city_data in address_data:
        city_code = city_data['code']
        city = city_model(code=city_code, name=city_data['name'])
        cities.append(city)

        for district_data in city_data['districts']:
            district_code = district_data['code']
            districts.append(district_model(code=district_code,
                                            name=district_data['name'],
                                            city_id=city_code))
            for ward_data in district_data['wards']:
                wards.append(
                    ward_model(code=ward_data['code'],
                               name=ward_data['name'],
                               district_id=district_code))

    city_model.objects.bulk_create(cities)
    district_model.objects.bulk_create(districts)
    ward_model.objects.bulk_create(wards)


def delete_all_address(apps, schema_editor):
    city_model = apps.get_model("api_address", "City")
    district_model = apps.get_model("api_address", "District")
    ward_model = apps.get_model("api_address", "Ward")

    city_model.objects.all().delete()
    district_model.objects.all().delete()
    ward_model.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('api_address', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_address, delete_all_address)
    ]