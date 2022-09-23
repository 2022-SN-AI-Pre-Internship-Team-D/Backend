from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns =[
    path('', views.getRoutes),

    path('sign-up', views.SignupView.as_view(), name='token'),
    path('sign-in', views.MyTokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('<user_uuid>/info', views.get_info, name='get_info'),
    path('<user_uuid>/exist', views.user_exist_db, name='check_user_exist_db'),
]


