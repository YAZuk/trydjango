from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=1024, default="")
    content = models.TextField(default="")

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.title
