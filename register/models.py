from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    password = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return self.username
