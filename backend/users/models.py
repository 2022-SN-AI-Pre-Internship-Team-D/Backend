from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True, unique=True)
    is_active = models.IntegerField(default=1)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'

