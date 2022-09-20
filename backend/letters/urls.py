from django.urls import path
from . import views

urlpatterns =[
    path('users/<user_uuid>/events/<event_uuid>/all/pages/<page_number>',views.get_letters),
    path('users/<user_uuid>/birth/all/pages/<page_number>',views.get_birth_letters),
    path('users/<user_uuid>/events/<event_uuid>/write',views.write_letter),
    path('users/<user_uuid>/birth/write',views.birth_write_letter),
    path('users/<user_uuid>/events/all/counts',views.get_all_events_cnt),
    path('users/<user_uuid>/birth/counts',views.get_birth_cnt),
    path('users/<user_uuid>/events/<event_uuid>/counts',views.get_event_cnt),
    path('events/<event_uuid>/check-date',views.check_date),
    path('users/<user_uuid>/events/birth/check-birth-date',views.check_birth_date),
    path('events/all',views.get_all_event_info),
    path('users/<user_uuid>/birth',views.get_user_birth_info),
    
]