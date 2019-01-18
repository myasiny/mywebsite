from datetime import datetime

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
