from django.shortcuts import render
from apps.catalogs.models import Product

# Create your views here.
def products_list(request):
    products = Product.objects.filter(publish_at__isnull=False).order_by('description')
    return render(request, 'catalogs/products_list.html', {'products': products})