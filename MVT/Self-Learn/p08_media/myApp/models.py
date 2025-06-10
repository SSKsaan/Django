from django.db import models

# Create your models here.

class myModel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/', blank=True) # goes in project
    pic = models.ImageField(upload_to='myApp/media/', blank=True) # goes in app

    def __str__(self):
        return self.name