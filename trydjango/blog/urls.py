from django.urls import path
from .views import (
                    ArticleListView,
                    ArticleDetailView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView,
                    BaseView,
                    BaseDetailView, TestAPIView,
                    TestAPIView1
                    )


app_name = 'articles'

urlpatterns = [
                # path('', blog_home, name="blog-home"),
                path('', ArticleListView.as_view(), name="article-list"),
                path('<int:pk>/', ArticleDetailView.as_view(), name="article-detail"),
                path('<int:pk>/update', ArticleUpdateView.as_view(), name="article-update"),
                path('<int:pk>/delete', ArticleDeleteView.as_view(), name="article-delete"),
                path('create/', ArticleCreateView.as_view(), name="article-create"),
                path('about/', BaseView.as_view(template_name="articles/contact.html"), name="article-about"),
                path('about/<int:pk>', BaseDetailView.as_view(), name="article-about-detail"),
                path('test/', TestAPIView.as_view(), name="article-test"),
                path('test1/', TestAPIView1.as_view(), name="article-test1"),
               ]
