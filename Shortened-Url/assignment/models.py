from __future__ import unicode_literals

from django.db import models


# Create your models here.

class ShortUrl(models.Model):
    long_url = models.CharField(max_length=2500)
    short_url = models.CharField(max_length=32, unique=True)
    last_checked = models.DateTimeField(auto_now_add=True)
    no_of_views = models.PositiveIntegerField(default=0)
    redirect_location = models.CharField(max_length=2500, default='')

    def __str__(self):
        return self.short_url

    class Meta:
        ordering = ['-pk']
