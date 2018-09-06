from django.shortcuts import render
from django.views.generic import (
                                    CreateView,
                                    DetailView,
                                    ListView,
                                    UpdateView,
                                    DeleteView
                                    )
# Create your views here.

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()





