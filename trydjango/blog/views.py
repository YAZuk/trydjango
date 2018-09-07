from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import (
        ListView,
        CreateView,
        DetailView,
        UpdateView,
        DeleteView
)
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


from .serializers import ArticleSerializer


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
    authentication_classes = [SessionAuthentication]


class TestCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [SessionAuthentication]


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
