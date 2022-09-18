from django.db import models

# Create your models here.

class S3(models.Model):
    title = models.CharField(max_length = 200)
    photo = models.FileField()
    def __str__(self):
        return self.photo