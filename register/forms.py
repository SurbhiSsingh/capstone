from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

DOMAIN_CHOICES = [
    ('iiitd.ac.in', 'iiitd.ac.in'),
    ('alum.iiitd.ac.in', 'alum.iiitd.ac.in'),  # optional backup domain
]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'phone']  # ✅ Fixed
        
class RegistrationForm(UserCreationForm):
    email_domain = forms.ChoiceField(
        choices=DOMAIN_CHOICES,
        label='Email Domain'
    )
    phone = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser   # ✅ Fix yeh hai
        fields = ['username', 'email_domain', 'phone', 'password1', 'password2']
        
class StudentRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    email_domain = forms.ChoiceField(choices=[
        (settings.PRIMARY_EMAIL_DOMAIN, settings.PRIMARY_EMAIL_DOMAIN),
        (settings.BACKUP_EMAIL_DOMAIN, settings.BACKUP_EMAIL_DOMAIN),
    ], label="Select Email Domain")
    otp = forms.CharField(max_length=6, required=False, label="Enter OTP")
