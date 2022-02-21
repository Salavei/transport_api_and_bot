
from django.contrib import admin
from django.urls import path
from .views import first_page
from ugc.views import TransportSerializerView, StationSerializerView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'infotrans', TransportSerializerView, basename='infotrans')
router.register(r'infostation', StationSerializerView, basename='infostation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first_page),
]

urlpatterns += router.urls