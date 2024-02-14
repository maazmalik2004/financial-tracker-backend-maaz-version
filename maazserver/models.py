# maazserver/models.py
from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        app_label = 'maazbackend'
