from django.urls import path
from .views import ViewGetInfoUser


urlpatterns = [
        path('', ViewGetInfoUser.as_view(), name="employee-info"),
]
