from django.contrib import admin
from apps.catalogs.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)
# Register your models here.
