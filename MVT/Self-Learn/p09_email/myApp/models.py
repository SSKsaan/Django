from django.db import models

# Create your models here.
class Email_Model(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=500)
    content = models.TextField()

    def __str__(self):
        return self.subject