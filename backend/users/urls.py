from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns =[
    path('', views.getRoutes),

    path('sign-up/', views.SignupView.as_view(), name='token'),
    path('sign-in/', views.MyTokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('<user_uuid>/get-birth/', views.get_birth, name='get_birth'),
    path('<user_uuid>/get-username/', views.get_username, name='get_username'),
    path('<user_uuid>/get-image/', views.get_image, name='get_image'),

]