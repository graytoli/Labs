from django.db import models

class LongURL(models.Model):
    url = models.TextField()
    code = models.CharField(max_length=8)