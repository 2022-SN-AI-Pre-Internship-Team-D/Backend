from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import user

# Create your views here.


def signup(request):   #회원가입
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        #key 값에 값 넣기, value없으면 none반환
        username = request.POST.get['username',None]  
        email = request.POST.get['email',None]
        password = request.POST.get['password',None]
        re_password = request.POST.get['re_password',None]
        birth = request.POST.get['birth',None]
        res_data = {} 

        #생일도 필수 입력값으로 함!!?
        if not (username and email and password and re_password and birth) :
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password :
            #return HttpResponse('비밀번호가 다릅니다.')
            #return Response(status=status.HTTP_204_NO_CONTENT)
            #res_data['error'] = '비밀번호가 다릅니다.'
            return JsonResponse({'error': 'password not match'}, status=400)
        elif user.filter(email = data['email']).exists() :
            res_data['error'] = 'duplicated email'
            #return Response({'error': 'duplicated email'}, status=HTTP_400_BAD_REQUEST)
            return Response(status=HTTP_400_BAD_REQUEST)
        else :
            user = user(username=username, email=email, password=make_password(password), birth=birth) #make_password 괄호에 들어간 비밀번호 문자열 암호화
            user.save()
            return Response(status='complete')
      

def signin(request):        #로그인
    response_data = {}

    if request.method == "GET" :
        return render(request, 'signin.html')

    elif request.method == "POST":
        signin_username = request.POST.get('username', None)
        signin_password = request.POST.get('password', None)


        if not (signin_username and signin_password):
            response_data['error']="아이디와 비밀번호를 모두 입력해주세요."
        else : 
            user = user.objects.get(username=signin_username) 
            #db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(signin_password, user.password):
                request.session['user'] = user.id 
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
                return Response({'error': 'invalid_user'}, status= status.HTTP_401_BAD_REQUEST)
        

        return render(request, 'signin.html',response_data)


def logout(request):
    request.session.pop('user')
    return redirect('/')