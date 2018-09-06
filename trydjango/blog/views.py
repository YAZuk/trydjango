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
