# Generated by Django 3.2.8 on 2022-03-02 15:50

import api_account.models.Role
import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone
import djongo.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('avatar', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role', djongo.models.fields.EmbeddedField(model_container=api_account.models.Role.Role)),
            ],
            options={
                'db_table': 'account',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'role',
            },
        ),
    ]
