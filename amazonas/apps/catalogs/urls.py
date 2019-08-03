from django.urls import path
from apps.catalogs.views import products_list

urlpatterns = [
    path('products/', products_list, name="products-list")
]