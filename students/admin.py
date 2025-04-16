from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone","course","branch","start","end")
    prepopulated_fields = {"slug": ("name",)}