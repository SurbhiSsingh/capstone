from django.db import models

class Publication(models.Model):
    CATEGORY_CHOICES = [
        ('journal', 'Journal'),
        ('conference', 'Conference'),
        ('patent', 'Patent'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    topic = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title