from django.shortcuts import render, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, GenericAPIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.db.models import QuerySet
from .serializers import SerializerGetInfoUser
from .models import UserInfo
from django.http import HttpResponse
from rest_framework.views import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
import re
from rest_framework import status
# Create your views here.


class TestException(Exception):
    """
        test exception
    """


class ViewGetInfoUserTest(ModelViewSet):
    queryset = User.objects.all()


class ViewGetInfoUser(CreateAPIView):
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()
    serializer_class = SerializerGetInfoUser

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=False):
            # формат телефона должен быть +79995672345
            try:
                serializer.data['phone']
            except KeyError:
                return Response(data={'Json': 'error'}, status=status.HTTP_400_BAD_REQUEST)

            phone_is_valid = re.search('\+\d{11}', serializer.data['phone'])

            if phone_is_valid is None:
                return Response(data={'Phone': 'is valid'}, status=status.HTTP_400_BAD_REQUEST)

            phone_exists = UserInfo.objects.filter(phone=phone_is_valid.string).exists()

            if phone_exists:
                return Response(data={'Phone': 'exists'}, status=status.HTTP_400_BAD_REQUEST)
            UserInfo.objects.create(username=serializer.data['username'], age=serializer.data['age'],
                                    email=serializer.data['email'], summary=serializer.data['summary'],
                                    phone=phone_is_valid.string)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

