from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from api import views

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user/', views.UserCreateApiView.as_view(), name='user'),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/test/', views.CategoryTestView.as_view(),
         name='category_test'),
]
