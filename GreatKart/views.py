from django.shortcuts import render
from store.models import *
def index(request):
    all_products = ProductModel.objects.all().filter(product_is_available = True).order_by('-product_created_date')
    context = {
        'all_products': all_products
    }
    return render(request, 'GreatKart/index.html', context)