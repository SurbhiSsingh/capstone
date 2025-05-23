from django.db import models
from django.urls import reverse
from cms.models.pluginmodel import CMSPlugin


class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NewsItem(models.Model):
    headline = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.headline
    
    
    ################################################
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.pk)])
