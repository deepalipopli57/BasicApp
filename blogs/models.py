from django.db import models

# Create your models here.
from django.urls import reverse


class BlogsModel(models.Model):
    title = models.CharField(max_length=40, blank=True)
    text = models.TextField(max_length=200, blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return(self.title)

