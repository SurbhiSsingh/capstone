# mission/admin.py

from django.contrib import admin
from .models import MissionVision

@admin.register(MissionVision)
class MissionVisionAdmin(admin.ModelAdmin):
    list_display = ['title', 'last_updated']
