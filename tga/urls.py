from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('live_videos.urls'), name='videos_page'),
    path('api/', include('ugc.urls'), name='api_page'),
]