from django.urls import path
from . import views

urlpatterns = [
    path('phd/', lambda r: views.team_list(r, 'phd'), name='team_phd'),
    path('mtech/', lambda r: views.team_list(r, 'mtech'), name='team_mtech'),
    path('btech/', lambda r: views.team_list(r, 'btech'), name='team_btech'),
    path('alumni/', lambda r: views.team_list(r, 'alumni'), name='team_alumni'),
    path('add/', views.add_member, name='add_team_member'),
]