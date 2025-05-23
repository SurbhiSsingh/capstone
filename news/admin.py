from django.contrib import admin
from .models import NewsItem
from .models import News

admin.site.register(NewsItem)
admin.site.register(News)
