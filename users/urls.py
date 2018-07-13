from django.conf import settings
from django.conf.urls import include, url
from django.contrib.staticfiles import views

from users.api import views as api_views

from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

# Define the API URLs
router = DefaultRouter()

# Standard CRUD operation APIs
router.register(r'users', api_views.UsersViewSet, base_name='users')

urlpatterns = [
    # Register the APIs
    url(r'^api/', include(router.urls)),

    # Include a authentication endpoint for the APIs
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # JSON JWT token URLS
    url(r'^api/login/$', obtain_jwt_token),
    url(r'^api/token-refresh/$', refresh_jwt_token),
]

# Addition of the media files URLs
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', views.serve, {
                                  'document_root': settings.MEDIA_ROOT})
    ]