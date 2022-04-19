# Generated by Django 3.2.8 on 2022-04-19 17:42

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_doctor', '0003_review'),
        ('api_user', '0003_migrate_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.TextField()),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='api_doctor.doctor')),
            ],
            options={
                'db_table': 'blog',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_activate', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('rate', models.FloatField(null=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='api_blog.blog')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='blog', to='api_user.user')),
            ],
            options={
                'db_table': 'comment',
                'ordering': ('created_at',),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]