from django.urls import path
from . import views

urlpatterns = [
    path('mission-vision/', views.mission_vision, name='mission_vision'),
]
