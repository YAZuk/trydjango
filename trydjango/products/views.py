from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views import View

from .models import Product
from .forms import ProductForm, RawProductForm
from django.urls import reverse
from django.forms import Form, ModelForm
# Create your views here.


def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "products/product_list.html", context)


def product_delete_view(request, id_product):
    product = get_object_or_404(Product, id=id_product)
    my_context = {
        "product": product,
    }
    # print(request.method)
    # if request.method == 'POST':
    product.delete()
    # redirect("../../../")
    return render(request, "products/product_delete.html", my_context)


def product_detail_view(request, id_product):
    product = get_object_or_404(Product, id=id_product)
    my_context = {
        "title": product.title,
        "price": product.price,
        "description": product.description
    }
    return render(request, "products/product_detail.html", my_context)


def homepage_view(request, *args, **kwargs):
    my_context = {
        "my_text": "text of my_text",
        "my_list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    }
    return render(request, "home.html", my_context)


def product_create_view_django_form(request):
    print(reverse())
    form = RawProductForm(request.GET)
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    context = {
        "form": form
    }
    return render(request, "products/product_create_django_form.html", context)


def product_create_view_raw(request):
    context = {
    }
    if request.method == "POST":
        print(request.POST.get('title'))
    return render(request, "products/product_create_raw.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
    form = ProductForm()
    context = {
        "form": form
    }
    return render(request, "products/product_create.html", context)


# def product_detail_view(request):
#     product = Product.objects.get(pk=20)
#     my_context = {
#         "title": product.title,
#         "price": product.price,
#         "description": product.description
#     }
#     return render(request, "products/product_detail.html", my_context)



# class ProductView(View):
#     def get(self, request):
#         pass
#
#     def post(self, request):
#         pass
