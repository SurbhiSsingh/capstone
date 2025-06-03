from django import forms
from .models import CustomUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import settings

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#4cb4a5] focus:border-transparent'
            })

DOMAIN_CHOICES = [
    ('iiitd.ac.in', 'iiitd.ac.in'),
    ('alum.iiitd.ac.in', 'alum.iiitd.ac.in'),  # optional backup domain
]


class CustomUserCreationForm(StyleFormMixin, UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        
        # Customize help texts
        self.fields['username'].help_text = 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        self.fields['password1'].help_text = 'Your password must contain at least 8 characters.'
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'

class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone']
        
class ProfileUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'phone']  # ✅ Fixed
        
class RegistrationForm(StyleFormMixin, UserCreationForm):
    email_domain = forms.ChoiceField(
        choices=DOMAIN_CHOICES,
        label='Email Domain'
    )
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )

    class Meta:
        model = CustomUser   # ✅ Fix yeh hai
        fields = ['username', 'email_domain', 'phone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Choose a username'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})
        
class StudentRegistrationForm(StyleFormMixin, forms.Form):
    username = forms.CharField(
        max_length=100,
        label="Username",
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
    )
    email_domain = forms.ChoiceField(
        choices=[
            (settings.PRIMARY_EMAIL_DOMAIN, settings.PRIMARY_EMAIL_DOMAIN),
            (settings.BACKUP_EMAIL_DOMAIN, settings.BACKUP_EMAIL_DOMAIN),
        ],
        label="Select Email Domain"
    )
    otp = forms.CharField(
        max_length=6,
        required=False,
        label="Enter OTP",
        widget=forms.TextInput(attrs={'placeholder': 'Enter 6-digit OTP'})
    )
