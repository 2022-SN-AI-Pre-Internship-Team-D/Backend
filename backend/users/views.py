from django.shortcuts import render
from letters.models import letter, anniversary
from .models import User
from letters import utils
from .serializers import SignupSirializer

from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSirializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_uuid'] = str(user.uuid)

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'sign-up/',
        'sign-in/',
        'token/refresh/',
        'token/verify/',
    ]
    return Response(routes)

@api_view(['GET'])
def get_birth(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    birth = User.objects.get(id=user_id).birth
    # serializer = UserSerializer(birth, many=True)
    return Response(birth)

@api_view(['GET'])
def get_username(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    username = User.objects.get(id=user_id).username
    return Response(username)

@api_view(['GET'])
def get_image(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    image = User.objects.get(id=user_id).image
    return Response(image)
