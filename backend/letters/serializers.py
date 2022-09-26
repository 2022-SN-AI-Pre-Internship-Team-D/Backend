from rest_framework import serializers
from .models import letter, anniversary
from users.models import User

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
        return model_instance['anni_id']

    def get_count(self, model_instance):
        return model_instance['count']

#mainpage 추가할 부분

class EventSerializer(serializers.Serializer):
    ##기념일 테이블에서 뭘 가져오는 걸 명시하니 위에 세개는 맞습니다! 하지만 user_uuid는 유저테이블에 있겠죠..?

    uuid = serializers.UUIDField(),
    name = serializers.CharField(),
    date = serializers.DateField(),

    class Meta:
        model = anniversary
        fields = '__all__'
    
    def get_uuid(self, model_instance):
        return model_instance.event_uuid
    def get_name(self, model_instance):
        return model_instance.event_name
    def get_date(self, model_instance):
<<<<<<< HEAD
        return model_instance.event_date
    
   

#이부분은 유저 테이블에
    # def get_user_uuid(self, model_instance):
    #     return model_instance['user_uuid']

=======
        return model_instance['event_date']
    def get_user_uuid(self, model_instance):
        return model_instance['user_uuid']
    
>>>>>>> a41944474883f2fde4e657e901e87f38d9bef641
        #밑에거는 또같이
    
#변수에서 필드 이름은 models.py참고 / 
#user id , event 부분을 하나의 serializer에 추가
#기념일 + 생일 테이블
#모든 필드가 필요한지

