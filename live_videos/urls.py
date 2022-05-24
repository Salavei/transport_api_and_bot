from django.urls import path
from . import views

urlpatterns = [
    path('', views.pants_page, name='pants_page'),
    path('car/', views.car_page, name='car_page'),
]
