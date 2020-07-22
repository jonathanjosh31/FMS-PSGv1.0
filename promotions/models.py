from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=264)
    images = models.ImageField(upload_to='promotions/')
