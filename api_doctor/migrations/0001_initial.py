# Generated by Django 3.2.8 on 2022-03-21 11:26

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('detail_address', models.CharField(blank=True, max_length=200, null=True)),
                ('ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clinic', to='api_address.ward')),
            ],
            options={
                'db_table': 'clinic',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'department',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('detail_address', models.CharField(blank=True, max_length=200, null=True)),
                ('ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital', to='api_address.ward')),
            ],
            options={
                'db_table': 'hospital',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('detail_address', models.CharField(blank=True, max_length=200, null=True)),
                ('joined_date', models.DateField(blank=True, null=True)),
                ('certificate', models.CharField(blank=True, max_length=50, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('clinic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='api_doctor.clinic')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='api_doctor.department')),
                ('hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='api_doctor.hospital')),
                ('ward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='api_address.ward')),
            ],
            options={
                'db_table': 'doctor',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
