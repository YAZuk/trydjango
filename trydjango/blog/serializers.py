from rest_framework import serializers
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.serializers import ModelSerializer
from .models import Article


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = ['title', 'content']
