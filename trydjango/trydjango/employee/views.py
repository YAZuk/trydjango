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
# Create your views here.


class ViewGetInfoUserTest(ModelViewSet):
    queryset = User.objects.all()
    # serializer_class =


class ViewGetInfoUser(CreateAPIView):
    """
        :arg
        :param
        :return
        :parameter
    """
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserInfo.objects.all()
    serializer_class = SerializerGetInfoUser

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        # username = serializer.validated_data['username']
        # email = serializer.validated_data['email']
        # age = serializer.validated_data['age']
        if serializer.is_valid(raise_exception=True):
            UserInfo.objects.create(username=serializer.data['username'], age=serializer.data['age'],
                                    email=serializer.data['email'], summary=serializer.data['summary'])
            return Response(serializer.data)
            # return HttpResponseRedirect(serializer.data, redirect_to="/")
        return Response(status=401)

