from django.db import models

# Create your models here.
class PostModel(models.Model):
    text = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return (self.text[:50])