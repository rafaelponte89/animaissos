"""animaissos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from animaissos.settings import MEDIA_URL
from app_animais.views import getCampanhasAtivas
from .views import index

schema_url_patterns = [
    path('api/v1/', include('api_animais.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('', include('app_animais.urls')),
    path('api/v1/', include('api_animais.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # Documentação
    path('openapi', get_schema_view(
         title="AnimaisSOS",
         description="API for all things …",
         version="1.0.0",
         patterns=schema_url_patterns
         ), name='openapi-schema'),

    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
