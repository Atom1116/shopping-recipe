from django.urls import path
from django.urls.conf import include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from api import views

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('csrf/', views.CsrfApiView.as_view()),
    path('create_user/', views.UserCreateApiView.as_view(),
         name='create_user'),
    path('login/', views.LoginApiView.as_view(), name="login"),
    path('logout/', views.LogoutApiView.as_view(), name="logout"),
    path('category/', views.CategoryListView.as_view(), name='category'),
    path('category/test/', views.CategoryTestView.as_view(),
         name='category_test'),
]
