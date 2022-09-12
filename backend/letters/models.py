from django.db import models
from users.models import user
import uuid

class anniversary(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=30)
    date = models.DateTimeField()
    user_id = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'anniversary'


class letter(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    anni_id = models.ForeignKey(anniversary, on_delete=models.CASCADE, db_column='anni_id')
    text = models.CharField(unique=True, max_length=255)
    file = models.CharField(unique=True, max_length=255)
    is_active = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'letter'