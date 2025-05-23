from django.contrib import admin
from .models import Faculty, ResearchInterest, TeachingInterest, Affiliation

# Faculty admin with autocomplete for ManyToManyFields
@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'email', 'phone')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('research_interests', 'teaching_interests', 'affiliations')

# Register and enable search for each related model

@admin.register(ResearchInterest)
class ResearchInterestAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(TeachingInterest)
class TeachingInterestAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Affiliation)
class AffiliationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

