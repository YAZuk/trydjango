from django.db import models

# Create your models here.


class Product(models.Model):

    title = models.CharField(max_length=256)
    description = models.TextField(max_length=256, blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    summary = models.TextField(max_length=256)
    featured = models.BooleanField()

    def __str__(self):
        return self.title + "(" + self.description + ")"