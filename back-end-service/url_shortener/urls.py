from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authentication import TokenAuthentication
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


schema_view = get_schema_view(
    openapi.Info(
        title="URL Shortener",
        default_version='v1.0.0',
        description="URL Shortener Server",
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[TokenAuthentication],
)

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/shortener/', include('shortener.urls')),
    re_path(r'^api/doc(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    path('api/doc/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
]

urlpatterns += staticfiles_urlpatterns()
