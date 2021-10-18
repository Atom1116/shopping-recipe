from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls))
]
