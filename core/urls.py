"""Base URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="DoctorZ Project API",
      default_version='v1',
      description="DoctorZ Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="huyviet2582000@gmail.com"),
      license=openapi.License(name="DoctorZ License hehe"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r"api/v1/base/", include('api_base.urls')),
    url(r"api/v1/user/", include('api_user.urls')),
    url(r"api/v1/account/", include('api_account.urls')),
    url(r"api/v1/admin/", include('api_admin.urls')),
    url(r"api/v1/doctor/", include('api_doctor.urls')),
    url(r"api/v1/address/", include('api_address.urls')),
    url(r"api/v1/blog/", include('api_blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
