
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from . import settings
from myapi import views, models


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'shots', views.ShotViewSet, basename='MyScreens')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)