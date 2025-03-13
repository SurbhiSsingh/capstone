from django.db import models
from django.utils.text import slugify
class Student(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=10,unique=True, blank=True)
    course= models.CharField(max_length=200,null=True, blank=True)
    branch = models.CharField(max_length=100, null=True, blank=True)
    start= models.DateField(null=True)
    end= models.DateField(null=True)  
    # author = models.CharField(max_length=100)
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_photo = models.ImageField(upload_to='students_photos/', default='default_profile.jpg')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
