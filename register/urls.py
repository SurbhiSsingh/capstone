from django.urls import path
from .views import register, login_view, profile, edit_profile
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),  # ✅ Use a single login path
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),  # ✅ Add logout functionality
    path("profile/", profile, name="profile"),
    path("edit-profile/", edit_profile, name="edit_profile"),
    path('register/', views.student_registration, name='student_registration'),
    path('register/', views.register, name='register'),
    # path('verify-otp/', views.verify_otp, name='verify_otp'),
   
 

]
