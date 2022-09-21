from ctypes import util
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from http.client import HTTPResponse
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import letter, anniversary
from users.models import User
from . import utils
from uuid import uuid4

from .serializers import UserInfoSerializer, AnniversaryInfoSerializer, LetterSerializer, LetterCountSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


@api_view(['GET'])
def get_letters(request, user_uuid, event_uuid, page_number):
    user_id = utils.get_user_id(user_uuid)
    event_id = utils.get_event_id(event_uuid)
    letters = letter.objects.filter(
        user_id=user_id, anni_id=event_id, is_active=1).order_by('-created_at')
    paginator = Paginator(letters, 5)
    page = page_number
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        return Response(status=status.HTTP_204_NO_CONTENT)
    except EmptyPage:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = LetterSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_birth_letters(request, user_uuid, page_number):
    user_id = utils.get_user_id(user_uuid)
    letters = letter.objects.filter(
        user_id=user_id, anni_id__isnull=True, is_active=1).order_by('-created_at')
    paginator = Paginator(letters, 5)
    page = page_number
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        return Response(status=status.HTTP_204_NO_CONTENT)
    except EmptyPage:
        return Response(status=status.HTTP_204_NO_CONTENT)
    serializer = LetterSerializer(contacts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def write_letter(request, user_uuid, event_uuid):
    user = utils.get_user(user_uuid)
    event = utils.get_event(event_uuid)
    text = request.POST.get('text')
    file = request.FILES.get('file')
    media = request.FILES.get('media')
    uuid = str(uuid4())
    file_url = utils.get_file_url(file, uuid)
    media_url = utils.get_file_url(media, uuid, input_type="media")
    letter.objects.create(uuid=uuid, user_id=user, anni_id = event, text=text, file=file_url, media=media_url)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def birth_write_letter(request, user_uuid):
    user = utils.get_user(user_uuid)
    text = request.POST.get('text')
    file = request.FILES.get('file')
    media = request.FILES.get('media')
    uuid = str(uuid4())
    file_url = utils.get_file_url(file, uuid)
    media_url = utils.get_file_url(media, uuid, input_type="media")
    letter.objects.create(uuid=uuid, user_id=user, text=text, file=file_url, media=media_url)
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_events_cnt(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    letters = letter.objects.filter(user_id=user_id, anni_id__isnull=False).values('anni_id').annotate(count=Count('anni_id'))
    serializer = LetterCountSerializer(letters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_event_cnt(request, user_uuid, event_uuid):
    user_id = utils.get_user_id(user_uuid)
    event_id = utils.get_event_id(event_uuid)
    letters = letter.objects.filter(user_id=user_id, anni_id=event_id).values('anni_id').annotate(count=Count('anni_id'))
    serializer = LetterCountSerializer(letters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_birth_cnt(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    letters = letter.objects.filter(user_id=user_id,anni_id__isnull=True).values('anni_id').annotate(count=Count('user_id'))
    serializer = LetterCountSerializer(letters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def check_birth_date(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    now = datetime.now().date()
    birth = User.objects.get(id=user_id).birth
    birth = date(2022, birth.month, birth.day)
    if birth == now:
        return JsonResponse({"status": "true"})
    elif birth > now:
        date_diff = birth - now
        return JsonResponse({"status": "false", "days":date_diff.days})
    elif birth < now:
        tmp_birth = birth + relativedelta(years=1)
        date_diff = tmp_birth - now 
        return JsonResponse({"status": "false", "days":date_diff.days})

@api_view(['GET'])
def check_date(request, event_uuid):
    event_id = utils.get_event_id(event_uuid)
    now = datetime.now().date()
    date = anniversary.objects.get(id=event_id).date

    if date == now:
        return JsonResponse({"status": "true"})
    elif date > now:
        date_diff = date - now
        return JsonResponse({"status": "false", "days":date_diff.days})
    elif date < now:
        tmp_date = date + relativedelta(years=1)
        date_diff = tmp_date - now 
        return JsonResponse({"status": "false", "days":date_diff.days})

@api_view(['GET'])
def get_all_event_info(request):
    events = anniversary.objects.all()
    serializer = AnniversaryInfoSerializer(events, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_birth_info(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    events = User.objects.filter(id = user_id)
    serializer = UserInfoSerializer(events, many=True)
    return Response(serializer.data)
