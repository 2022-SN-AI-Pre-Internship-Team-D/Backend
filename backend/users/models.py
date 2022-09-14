from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True, unique=True)
    birth = models.DateField(blank=False)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'birth']

    class Meta:
        db_table = 'user'