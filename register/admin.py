from django.contrib import admin
from .models import CustomUser, Profile  # Ensure Profile exists in models.py

admin.site.register(CustomUser)
admin.site.register(Profile)
