from rest_framework import serializers
from .models import letter, anniversary

class letterSerializer(serializers.ModelSerializer):
    class Meta:
        model = letter
        fields = ("id", "uuid", "user_id", "anni_id", "text", "file", "is_active")

