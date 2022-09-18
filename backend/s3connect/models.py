from django.db import models

# Create your models here.

class S3(models.Model):
    photo = models.FileField()
    def __str__(self):
        return self.photo