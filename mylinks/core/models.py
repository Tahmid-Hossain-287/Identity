from django.db import models

# Create your models here.

class Link(models.Model):
    # title, url, icon_name
    title = models.CharField(max_length=100)
    url = models.URLField()
    icon_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    clicks = models.IntegerField(default=0)