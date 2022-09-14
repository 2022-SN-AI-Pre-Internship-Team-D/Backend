from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True, unique=True)
    birth = models.DateField(default=datetime.now)
    is_active = models.IntegerField(default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'