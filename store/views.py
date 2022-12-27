from django.shortcuts import render
from .models import *
# Create your views here.
def StoreHomepage(request, category_slug = None):
    if category_slug:
        category_sorted_products = ProductModel.objects.filter(product_category__category_slug = category_slug, product_is_available = True).order_by('-product_created_date')
        category_sorted_products_count = category_sorted_products.count()
        context = {
        'all_products':category_sorted_products,
        'all_products_count':category_sorted_products_count
        }
        return render(request, 'store/storehomepage.html',context)
    all_products = ProductModel.objects.all().filter(product_is_available = True).order_by('-product_created_date')
    all_products_count = all_products.count()
    context = {
        'all_products':all_products,
        'all_products_count':all_products_count
    }
    return render(request, 'store/storehomepage.html',context)

def DetailProductPage(request, category_slug = None, product_id = None):
    if product_id and category_slug:
        product = ProductModel.objects.get(product_category__category_slug = category_slug, id = product_id)
        out_of_stock = False
        if product.product_stock <=0:
            out_of_stock =True
        context = {
            'product':product,
            'out_of_stock':out_of_stock,
        }
        return render(request, 'store/detail_product.html',context)