from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=256, default="title")
    description = models.TextField(max_length=1024, default="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1.00)
    summary = models.TextField(default="summary")
    another = models.TextField(blank=False)
    other = models.TextField(null=False, default="default")

    def __str__(self):
        return "{} ({})".format(self.title, self.description)

