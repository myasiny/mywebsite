from django.db import models

from datetime import datetime


class Post(models.Model):
    title = models.CharField(blank=False, max_length=100)
    body = models.TextField(blank=False)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
