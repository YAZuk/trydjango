from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Product
from .forms import ProductForm, RawProductForm
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
    # products = get_list_or_404(Product)
    my_context = {
        "text": "Products:",
        "is_true": True,
        "my_list": [23, 32, 32, 43, 54, 65, 7, 65, 4323, 23, 'Abc'],
        "products": products
    }
    return render(request, "product_detail.html", my_context)


def product_id(request, my_id):
    # product = Product.objects.get(pk=my_id)
    product = get_object_or_404(Product, pk=my_id)
    # try:
    #     product = Product.objects.get(pk=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

    my_context = {
        "title": product.title,
        "description": product.description,
        "price": product.price,

    }
    return render(request, "product_detail_id.html", my_context)


def product_delete(request, my_id):
    product = get_object_or_404(Product, pk=my_id)
    if request.method == "POST":
        product.delete()
        return redirect("../../")

    my_context = {
        "text": my_id.__str__() + " " + "deleted"
    }

    return render(request, "product_delete.html", my_context)



# def product_create(request):
#     my_form = RawProductForm(request.GET)
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#     context = {
#             "form": my_form
#     }
#     return render(request, "product_create.html", context)


def product_create(request):
    initialize_values = {"title": "Inititlaize value"}
    form = ProductForm(request.POST or None, initial=initialize_values)
    if form.is_valid():
        form.save()
    context = {
        "form": form
    }
    return render(request, "product_create.html", context)


# def product_create(request):
#     if request.method == "POST":
#         new_title = request.POST.get('title')
#         print(new_title)
#
#     context = {
#     }
#     return render(request, "product_create.html", context)


def about(request, *args, **kwargs):
    return render(request, "about.html", {})
