# mission/models.py

from django.db import models

class MissionVision(models.Model):
    title = models.CharField(max_length=100, default="Mission & Vision")
    mission_text = models.TextField()
    vision_text = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
