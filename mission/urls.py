from django.urls import path
from . import views

urlpatterns = [
    path('', views.mission_vision, name='mission_vision'),
    path('add/', views.add_mission_vision, name='add_mission_vision'),
]