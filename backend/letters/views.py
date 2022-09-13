from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import letter, anniversary
from users.models import User
from .serializers import LetterSerializer, LetterCountSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import utils


class LetterViewAPI(APIView):
    def get(self, request, user_uuid, page_number):
        user_id = utils.get_user(user_uuid).id
        letters = letter.objects.filter(
            user_id=user_id, is_active=1).order_by('-created_at')
        paginator = Paginator(letters, 3)
        page = page_number
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            return Response(status=status.HTTP_204_NO_CONTENT)
        except EmptyPage:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = LetterSerializer(contacts, many=True)
        return Response(serializer.data)


class LetterAPI(APIView):
    def post(self, request, user_uuid, event_uuid):
        user = utils.get_user(user_uuid)
        event = utils.get_event(event_uuid)
        text = request.POST.get('text')
        file = request.FILES.get('file')
        letter.objects.create(
            user_id=user, anni_id=event, text=text, file=file)
        return Response(status=status.HTTP_200_OK)
