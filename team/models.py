from django.db import models

class TeamMember(models.Model):
    DEGREE_CHOICES = [
        ('phd', 'PhD'),
        ('mtech', 'MTech'),
        ('btech', 'BTech'),
        ('alumni', 'Alumni'),
    ]
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=10, choices=DEGREE_CHOICES)
    year = models.CharField(max_length=10, blank=True)
    current_affiliation = models.CharField(max_length=200, blank=True)
    profile_photo = models.ImageField(upload_to='team_photos/', blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name