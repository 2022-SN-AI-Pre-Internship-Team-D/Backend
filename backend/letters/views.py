from datetime import datetime, date
from dateutil.relativedelta import relativedelta

from http.client import HTTPResponse
from django.http import JsonResponse

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from .models import letter, anniversary
from users.models import User
from . import utils
from uuid import uuid4

from .serializers import LetterSerializer, LetterCountSerializer, EventSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# try:
#     comment = Comment.objects.get(pk=comment_id)
# except Comment.DoesNotExist:
#     comment = None



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
    letter.objects.create(uuid=uuid, user_id=user, anni_id = event, text=text, file=file_url, media=media)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def birth_write_letter(request, user_uuid):
    user = utils.get_user(user_uuid)
    text = request.POST.get('text')
    file = request.FILES.get('file')
    media = request.FILES.get('media')
    uuid = str(uuid4())
    file_url = utils.get_file_url(file, uuid)
    letter.objects.create(uuid=uuid, user_id=user, text=text, file=file_url, media=media)
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
    letters = letter.objects.filter(user_id=user_id, anni_id=event_id).values(
        'anni_id').annotate(count=Count('anni_id'))
    serializer = LetterCountSerializer(letters, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_birth_cnt(request, user_uuid):
    user_id = utils.get_user_id(user_uuid)
    letters = letter.objects.filter(user_id=user_id,anni_id__isnull=True).values(
        'anni_id').annotate(count=Count('user_id'))
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

#김수민 메인페이지 부분
#경로 / 객체 404
#user_uuid 추가
#기념일 테이블에서 모든 정보 가져오기
<<<<<<< HEAD
#/@api_view(['GET'])
#/def mainpage_info(request, user_uuid): 
=======
@api_view(['GET'])
def mainpage_info(request, user_uuid): 
    ## view랑 serializer 관계를 알고, serializer를 활용한 코드를 작성하셔야합니다
    ## serializer에 어떤 값을 넣고 그 값이 ser~를 통해서 우리가 원하는 속성들만 return 될 수 있도록 해주니
    ## 저희는 모든 이벤트 애들을 다 저장해서 그 애들의 이름,날짜,uuid만 얻으면 되니까
    ## 변수 = 기념일테이블.objects.all()
    ## 변수2 = eventserial~(변수, many=true)
    ## return response(변수2.data)
    ## 이렇게 진행하시면 됩니다!
>>>>>>> a41944474883f2fde4e657e901e87f38d9bef641

    #이 부분 추가이유
    # event = event.objects.filter(
    #     event = event, anni_id__isnull=True, is_active=1).order_by('created_at') #기념일로 수정
    
    #user 부분에서 생일 날짜와 uuid 데이터 가지고 오기

    #user_id = utils.get_event_id(user_uuid) #위와 같을 수도; 꼭 필요한지
#/    print("User.get.object")

#/    user_id = get_object_or_404(User, uuid = user_uuid )

#/    birth_date = User.objects.get(id=user_id).birth 

    #ERD 의 anniversary 테이블에서 모든 정보 가지고 오기
    #event_id = utils.get_event_id(event_uuid)

    #event = anniversary.objects.all() #user uuid 
#/    print("Event.get.object")
#/    event = get_object_or_404(anniversary, user_id=user_id)

    #변수 처리를 하여 birth_date 이렇게 했는데 왜 회색 글자가 뜨는 건지...??
    
#/    serializer = EventSerializer(event, many=True)
#/    return Response(serializer.data, user_id, event) #birth date 까지 추가해서 + uuid
    
    

    ##여기 수정하기!

    #return anniversary.objects.get(uuid = event_uuid).id
    
    #birth_date = User.objects.get(id=user_id).birth
    # user_id = utils.get_user_id(user_uuid)
    # birth_date = User.objects.get(id=user_id).birth
    # event_id = utils.get_event_id(event_uuid)
    # event_date = anniversary.objects.get(id=event_id).date
    # event_name = anniversary.objects.get(id=event_id).name
    
    #anniversary event 모두 가져오기

    #event_id = utils.get_user_id
    #event = anniversary.objects.all()
    #event_name = anniversary.objects.all()
        # {   

        #     # 'event_id' : event_id,
        #     # 'user_id' : user_id,
        #     # 'event_date' : event_date,
        #     # 'event_name' : event_name,
        #     # 'birth_date' : birth_date            
            
        # } 
        # )
#event table + user table ? 
@api_view(['GET'])
def mainpage_info(request,user_uuid):
    events = anniversary.objects.all()
    serializer = EventSerializer(events, many=True)
    #user_id = utils.get_event_id(user_uuid)

    return Response(serializer.data)
