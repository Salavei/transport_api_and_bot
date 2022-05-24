from ugc.views import TransportSerializerView, StationSerializerView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'infotrans', TransportSerializerView, basename='infotrans')
router.register(r'infostation', StationSerializerView, basename='infostation')
urlpatterns = router.urls
