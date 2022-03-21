# Generated by Django 3.2.8 on 2022-03-21 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'city',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='districts', to='api_address.city')),
            ],
            options={
                'db_table': 'district',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wards', to='api_address.district')),
            ],
            options={
                'db_table': 'ward',
                'ordering': ('name',),
            },
        ),
    ]
