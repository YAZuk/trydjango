from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=1024, default="")
    content = models.TextField(default="")
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.title
