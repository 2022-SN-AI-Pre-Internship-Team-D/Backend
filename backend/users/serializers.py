from django.shortcuts import render
from letters.models import letter, anniversary
from .models import User
from users.models import User
from letters import utils
from .serializers import *
from uuid import uuid4

from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import generics, status

class SignupSirializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True
    ),
    password = serializers.CharField(
        required=True,
        write_only = True,
    )
    password2 = serializers.CharField(
        write_only = True, required=True
    )
    birth = serializers.DateField(
        required=True
    )
    image = serializers.FileField(
        required=True,
        # use_url = True
    )

    uuid = str(uuid4())
    image = utils.get_file_url(image, uuid)
    # User.objects.create(uuid=uuid, user_id=user, text=text, file=file_url, media=media)
    
    # print(image)

    class Meta:
        model = User
        image = serializers.CharField()
        fields = ('username','email','password','password2','birth','image')
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "password" : "Password fields didn't match"
            })
        
        return data
# post로 로그인할때 다른 정보받아오고 파일 보내는 부분은 
# meta image필드 재정의! get image한다음에 

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            birth = validated_data['birth'],
            # image = validated_data['image']
        )
        # uuid = str(uuid4())

        user.image = validated_data['image']
        # user.image = validated_data['image_url']
        # user.image = utils.get_file_url(image, uuid)
        
        # image = utils.get_file_url(image, uuid)
        # user.objects.create(uuid=uuid, user_id=user, image=image)

        token = RefreshToken.for_user(user)
        user.set_password(validated_data['password'])
        user.refreshtoken = token
        user.save()
    
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "uuid", "username", "email", "password", "birth", "image", "is_active")