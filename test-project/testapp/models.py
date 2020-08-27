from django.db import models

class TextBlob(models.Model):
    text = models.CharField(max_length=200)
