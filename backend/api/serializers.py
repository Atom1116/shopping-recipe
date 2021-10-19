from django.contrib.auth import get_user_model
from rest_framework import serializers
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
