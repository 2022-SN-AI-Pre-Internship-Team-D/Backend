from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import letter, anniversary
from users.models import User
from . import utils

from .serializers import LetterSerializer, LetterCountSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


@api_view(['GET'])
def get_letters(self, request, user_uuid, event_uuid, page_number):
    user_id = utils.get_user_id(user_uuid)
    event_id = utils.get_event_id(event_uuid)
    letters = letter.objects.filter(
        user_id=user_id, anni_id=event_id, is_active=1).order_by('-created_at')
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

def write_letter(self, request, user_uuid, event_uuid):
    user = utils.get_user(user_uuid)
    event = utils.get_event(event_uuid)
    text = request.POST.get('text')
    file = request.FILES.get('file')
    letter.objects.create(
        user_id=user, anni_id=event, text=text, file=file)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_events_cnt(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    letters = letter.objects.filter(user_id=user_id).values(
        'anni_id').annotate(count=Count('anni_id'))
    serializer = LetterCountSerializer(letters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_event_cnt(request, user_uuid, event_uuid):
    user_id = utils.get_user_id(user_uuid)
    event_id = utils.get_event_id(event_uuid)
    letters = letter.objects.filter(user_id=user_id,anni_id=event_id).values(
        'anni_id').annotate(count=Count('anni_id'))
    serializer = LetterCountSerializer(letters, many=True)
    return Response(serializer.data)