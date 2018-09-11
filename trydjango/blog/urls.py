from django.urls import path
from django.conf.urls import url
from .views import (
                    ArticleListView,
                    ArticleDetailView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView,
                    BaseView,
                    BaseDetailView, TestAPIView,
                    TestListCreate, TestPutDelete, TestGet, TestCreate,
                    TestDelete, TestList, TestGetSerializer
                    )
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

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
                path('test_api_view/', TestAPIView.as_view(), name="article-test"),
                path('test_list/', TestList.as_view(), name="article-list"),
                path('test_list_create/', TestListCreate.as_view(), name="article-list-create"),
                path('test_put_delete/<int:pk>', TestPutDelete.as_view(), name="article-put-delete"),
                path('test_delete/<int:pk>', TestDelete.as_view(), name="article-delete"),
                path('test_get/<int:pk>', TestGet.as_view(), name="article-get"),
                path('test_create/', TestCreate.as_view(), name="article-create"),
                url('obtain_jwt/', obtain_jwt_token),
                url('verify_jwt/', verify_jwt_token),
                url('refresh_jwt/', refresh_jwt_token),
                url('test_serializer/', TestGetSerializer.as_view()),
                # url('test_obtain_jwt1/', CustomAuthToken.as_view()),
               ]
