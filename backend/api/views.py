from django.contrib.auth import authenticate, login, logout
from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response
from api import serializers
from core import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
import json
from django.http import JsonResponse
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
import pprint


# CSRFトークン発行View
class CsrfApiView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        return JsonResponse({'token': get_token(request)})


# ユーザー新規作成View
class UserCreateApiView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# ログインView
class LoginApiView(views.APIView):

    def post(self, request, *args, **kwargs):
        params = json.loads(request.body)
        # ログインユーザーの検証
        user = authenticate(email=params["email"], password=params["password"])
        # ユーザー情報の取得
        user = models.User.objects.get(email=params['email'])
        # セッションIDの付与
        login(request, user)
        return Response({'session': request.session.session_key})


# ログアウトApiView
class LogoutApiView(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


# カテゴリー一覧取得View
class CategoryListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = serializers.CategoryListSerializer
    queryset = models.Category.objects.all()

    def get(self, request, *args, **kwargs):
        pprint.pprint(self.request.user.id)
        return super().get(request, *args, **kwargs)


class CategoryTestView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = serializers.CategoryTestPostSerializer


class RecipeView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.RecipePostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        recipePost = serializer.save()

        pprint.pprint(vars(recipePost))

        return Response(status=status.HTTP_200_OK)
