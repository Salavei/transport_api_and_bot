from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/course/', views.api_course_page, name='api_course_page'),
    path('', views.pants_page, name='pants_page'),
]
