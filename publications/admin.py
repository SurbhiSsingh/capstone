from django.contrib import admin
from .models import Publication

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'authors')
    search_fields = ('title', 'authors', 'topic')
    list_filter = ('category', 'year')