from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
# Create your views here.


def home(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact(request, *args, **kwargs):
    product = Product.objects.get(pk=1)
    my_context = {
        "text": product.title + "(" + product.description + ")",
        "number": product.price
    }
    return render(request, "contact.html", my_context)


def product(request, *args, **kwargs):
    products = Product.objects.all()
    my_context = {
        "text": "products1",
        "is_true": True,
        "my_list": [23, 32, 32, 43, 54, 65, 7, 65, 4323, 23, 'Abc'],
        "products": products
    }
    return render(request, "product_detail.html", my_context)


def about(request, *args, **kwargs):
    return render(request, "about.html", {})
