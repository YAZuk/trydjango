from django.urls import path
from .views import (
            product_detail_view,
            product_list,
            product_create_view,
            product_create_view_django_form,
            product_create_view_raw,
            product_delete_view
)

urlpatterns = [
    path('product_create_view_django_form/', product_create_view_django_form, name="product-create-view-django-form"),
    path('product_create_raw/', product_create_view_raw, name="product-create-view-raw"),
    path('product_list/', product_list, name="product-list"),
    path('product_create/', product_create_view, name="product-create-view"),
    path('product_detail/<int:id_product>', product_detail_view, name="product-detail-view"),
    path('product_delete/<int:id_product>', product_delete_view, name="product-delete-view"),
]