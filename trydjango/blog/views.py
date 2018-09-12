from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import View
from rest_framework import mixins
from rest_framework.response import Response
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView
)

import json
from rest_framework.serializers import Serializer
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer, MultiPartRenderer, AdminRenderer
# Create your views here.
from .models import Article
from .forms import ArticleModelForm
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListCreateAPIView, ListAPIView, RetrieveAPIView, \
    DestroyAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication,\
    BaseAuthentication, SessionAuthentication, RemoteUserAuthentication, BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication,\
    BaseAuthentication,BaseJSONWebTokenAuthentication
from json import JSONDecoder, JSONEncoder, JSONDecodeError
from rest_framework.parsers import JSONParser

from rest_framework_jwt.views import (VerifyJSONWebToken, RefreshJSONWebToken)

from django.contrib.auth.models import User
from .serializers import ArticleSerializer, TestSerializer, UserSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters.filters import DateFilter



# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })

# class TestMixin():
#     def get(self):
#         pass
#     def post(self):
#         pass





class GetUsers(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]


class TestAPIView(APIView):
    permission_classes = []
    # authentication_classes = [JSONWebTokenAuthentication]
    # parser_classes = JSONParser

    def get(self, request):
        return HttpResponse('Get apiview')

    def post(self, request):
        return HttpResponse("Post apiview", status=300)


class TestListCreate(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication]
    renderer_classes = [AdminRenderer]
    # parser_classes = [JSONParser]

    def perform_create(self, serializer):
        if serializer.is_valid():
            Article.objects.create(**serializer.data)
            # print(serializer.data)

    # def get_queryset(self):
    #     pass


class TestList(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication]
    renderer_classes = [AdminRenderer]

class TestPutDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication]


class TestDelete(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication]


class TestGet(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]


class TestGetSerializer(CreateAPIView):
    permission_classes = [IsAuthenticated]
    # queryset = Article.objects.all()
    serializer_class = TestSerializer
    authentication_classes = [JSONWebTokenAuthentication]

    def get(self, request):
        return Response(data={})

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            return Response(data={"status": "ok"}, status=201)
        raise Exception("JSON is not validated")


class TestCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [JSONWebTokenAuthentication]

    # def post(self, request, *args, **kwargs):
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         # serializer.save(data=request.data)
    #         return Response(data=request.data)
    #     return Response(data={"status": "error"})


class BaseDetailView(View):
    template_name = "articles/about_detail.html"

    def get(self, request, id= None, *args, **kwargs):
        return render(request, self.template_name, {})


class BaseView(View):
    template_name = "articles/about.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class ArticleCreateView(CreateView):
    queryset = Article.objects.all()
    form_class = ArticleModelForm
    template_name = "articles/article_create.html"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    form_class = ArticleModelForm
    template_name = "articles/article_create.html"

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)


class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = "articles/article_list.html"


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)

    def get_success_url(self):
        return reverse("articles:article-list")


def blog_home(request):
    return HttpResponse('adsadadsadsasdads')
