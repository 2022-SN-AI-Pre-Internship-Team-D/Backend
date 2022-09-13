from django.urls import path
from . import views

urlpatterns =[
    path('users/<user_uuid>/pages/<page_number>',views.LetterViewAPI.as_view()),
    path('users/<user_uuid>/events/<event_uuid>/write',views.LetterAPI.as_view()),
]