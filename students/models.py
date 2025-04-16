from django.db import models
from django.utils.text import slugify

class Student(models.Model):
    name = models.CharField(max_length=200)
    # start = models.DateTimeField()  
    slug = models.SlugField(unique=True, blank=True, null=True)    
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)

    COURSE_CHOICES = [
        ('B.Tech', 'B.Tech'),
        ('M.Tech', 'M.Tech'),
        ('Ph.D', 'Ph.D'),
    ]
    course = models.CharField(max_length=6, choices=COURSE_CHOICES, default='B.Tech')
    branch = models.CharField(max_length=100, null=True, blank=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)  
    content = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    profile_photo = models.ImageField(upload_to='students_photos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug
            counter = 1
            while Student.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
