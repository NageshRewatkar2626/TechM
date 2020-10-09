"""Exercise3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from e3 import views
from django.views.generic import TemplateView
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', views.RouterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('',TemplateView.as_view(template_name='rest_api.html'),name='main'),
    path('save_data/',views.RouterDetails.as_view(),name='save_data'),
    path('check/',views.check,name='check'),
    path('view_data/',views.view_data,name='view_data'),
    path('update/',views.update,name='update'),
    path('data_update/',views.data_update,name='data_update'),
    path('delete/',views.delete,name='delete')
    
]
