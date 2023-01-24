from django.contrib import admin
from django.urls import path, include
from bot_app.views import TransportView, StationView
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'api/v1/infotrans', TransportView, basename='infotrans'),
router.register(r'api/v1/infostation', StationView, basename='infostation')

urlpatterns += router.urls
urlpatterns += staticfiles_urlpatterns()
