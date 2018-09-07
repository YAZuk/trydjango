from rest_framework import serializers
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer, Serializer
from .models import Article


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'content']


class TestSerializer(Serializer):

    firstname = serializers.CharField(max_length=128)
    lastname = serializers.CharField(max_length=128)
    age = serializers.IntegerField(max_value=200, min_value=18)
    birthday = serializers.DateTimeField()

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
