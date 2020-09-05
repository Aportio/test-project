from django.db import models

# Saved input text
class TextBlob(models.Model):
    text = models.CharField(max_length=200)
