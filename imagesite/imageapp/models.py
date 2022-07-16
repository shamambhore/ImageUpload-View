from distutils.command.upload import upload
from operator import mod
from django.db import models

# Create your models here.

class Images(models.Model):
    images = models.ImageField(upload_to="project_images")
    date = models.DateTimeField(auto_now_add=True)
    
