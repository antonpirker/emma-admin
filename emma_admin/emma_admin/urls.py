"""emma_admin URL Configuration

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
from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from web.viewsets import BookingViewSet, CustomerViewSet, PropertyViewSet, UnitViewSet

from django.contrib import admin
admin.site.site_header = "*Emma Wanderer Admin"
admin.site.site_title = "Emma Wanderer"
admin.site.index_title = "Campus administration"


router = routers.DefaultRouter()
router.register(r'property', PropertyViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
