# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.faculty_list, name='faculty_list'),
#     path('faculty/<int:faculty_id>/', views.faculty_detail, name='faculty_detail'),

# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.faculty_list, name='faculty_list'),
    path('faculty/<slug:slug>/', views.faculty_detail, name='faculty_detail'),
    path('affiliation/<slug:slug>/', views.affiliation_detail, name='affiliation_detail'),

]
