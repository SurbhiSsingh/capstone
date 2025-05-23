from django.db import models

class ResearchInterest(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TeachingInterest(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Affiliation(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='default-slug', unique=False, blank=True)  # unique=False temporarily

    def __str__(self):
        return self.name




class Faculty(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    profile_photo = models.ImageField(upload_to='faculty_photos/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    phd_details = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    web_profile = models.URLField(blank=True, null=True)
    office = models.CharField(max_length=100, blank=True, null=True)
    profile_description = models.TextField(blank=True, null=True)

    research_interests = models.ManyToManyField(ResearchInterest, blank=True)
    teaching_interests = models.ManyToManyField(TeachingInterest, blank=True)
    affiliations = models.ManyToManyField(Affiliation, blank=True)

    def __str__(self):
        return self.name
