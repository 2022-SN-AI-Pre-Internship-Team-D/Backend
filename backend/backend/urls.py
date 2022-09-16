from django.contrib import admin
from django.urls import path, include

<<<<<<< Updated upstream
=======
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from . import views

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="letterman APIs",
        default_version='v1',
        description="letterman porject",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(AllowAny,),

)
>>>>>>> Stashed changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/letters/', include('letters.urls')),
<<<<<<< Updated upstream
=======
    path('image', views.Image.as_view(), name='image'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
>>>>>>> Stashed changes
]