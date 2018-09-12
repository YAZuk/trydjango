from rest_framework import serializers
from .models import UserInfo





class SerializerGetInfoUser(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'age', 'email', 'summary']

    # username = serializers.CharField(max_length=256)
    # age = serializers.IntegerField()
    # email = serializers.EmailField(max_length=256)

