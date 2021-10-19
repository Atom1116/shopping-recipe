# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from api import serializers
from core import models


# ユーザー新規作成View
class UserCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer


# カテゴリー一覧取得View
class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CategoryListSerializer
    queryset = models.Category.objects.all()


class CategoryTestView(generics.CreateAPIView):
    serializer_class = serializers.CategoryTestPostSerializer
