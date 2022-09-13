from rest_framework import serializers
from .models import letter, anniversary

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = letter
        fields = ("id", "uuid", "user_id", "anni_id", "text", "file", "is_active")

class EventLetterStatisticsSerializer(serializers.Serializer):
    event = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = letter
        fields = '__all__'

    def get_kind(self, model_instance):
        return model_instance['event']

    def get_cnt(self, model_instance):
        return model_instance['count']

