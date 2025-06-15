from django.db import models
from django.core.exceptions import ValidationError

def validate_iiitd_email(value):
    """Custom validator to ensure email ends with 'iiitd.ac.in'."""
    if value and not value.endswith('@iiitd.ac.in'):
        raise ValidationError("Only emails with the domain 'iiitd.ac.in' are allowed.")


class Profile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(
        blank=True,
        null=True,
        validators=[validate_iiitd_email]  # Add the custom validator here
    )
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    password = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return self.username
