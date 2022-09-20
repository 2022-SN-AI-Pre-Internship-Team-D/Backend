from users.models import User
from rest_framework import serializers
from .models import letter, anniversary
from .utils import get_event_name

class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = letter
        fields = ("id", "uuid", "user_id", "anni_id", "text", "file", "media")

class LetterCountSerializer(serializers.Serializer):
    event = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    class Meta:
        model = letter
        fields = '__all__'

    def get_event(self, model_instance):
        tmp = model_instance['anni_id']
        if not tmp:
            return "birth"
        return get_event_name(tmp)

    def get_count(self, model_instance):
        return model_instance['count']


class AnniversaryInfoSerializer(serializers.Serializer):
    event = serializers.SerializerMethodField()
    uuid = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = anniversary
        fields = '__all__'
    
    def get_event(self, model_instance):
        return model_instance.name

    def get_uuid(self, model_instance):
        return model_instance.uuid
    
    def get_date(self, model_instance):
        date = str(model_instance.date)
        return date[5:]

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "birth")
