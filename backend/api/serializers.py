from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import MaterialPostModel, RecipePost
from core import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'user_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class CategoryListSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    class Meta:
        model = models.Category
        fields = ('category_id', 'name',)


class CategoryTestPostSerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = models.Category
        fields = ('category_id', 'name')

    def create(self, validated_data):
        print(validated_data)
        return models.Category.objects.get(pk=1)


# 投稿材料シリアライザー
class MaterialPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
    unit = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return MaterialPostModel(**validated_data)


# レシピ投稿シリアライザー
class RecipePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    # recipe_image = serializers.ImageField()

    materials = serializers.ListField(
        child=MaterialPostSerializer()
    )

    # procedures = serializers.ListField(
    #     child=MaterialPostSerializer()
    # )

    def create(self, validated_data):
        return RecipePost(**validated_data)
