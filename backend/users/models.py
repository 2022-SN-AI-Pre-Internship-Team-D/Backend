from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# class user(models.Model):
#     id = models.AutoField(primary_key=True)
#     uuid = models.UUIDField(default=uuid.uuid4, editable=False)
#     nickname = models.CharField(unique=True, max_length=30)
#     email = models.CharField(unique=True, max_length=100)
#     password = models.BinaryField(max_length=60)
#     salt = models.BinaryField(max_length=29)
#     is_active = models.IntegerField(default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'member'

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True, unique=True)
    is_active = models.IntegerField(default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'