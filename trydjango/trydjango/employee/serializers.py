from rest_framework import serializers
from .models import UserInfo


class SerializerGetInfoUser(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'age', 'email', 'summary', 'phone']
