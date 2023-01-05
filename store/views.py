from django.shortcuts import render
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.
def StoreHomepage(request, category_slug = None):
    if category_slug:
        category_sorted_products = ProductModel.objects.filter(product_category__category_slug = category_slug, product_is_available = True).order_by('-product_created_date')
        paginator = Paginator(category_sorted_products, 5) # Among all products it will choose first 6 of them
        page = request.GET.get('page') # This will get page number from url of browser.
        paged_products = paginator.get_page(page)
        category_sorted_products_count = category_sorted_products.count()
        context = {
        'all_products':paged_products,
        'all_products_count':category_sorted_products_count
        }
        return render(request, 'store/storehomepage.html',context)
    all_products = ProductModel.objects.all().filter(product_is_available = True).order_by('-product_created_date')
    paginator = Paginator(all_products, 5) # Among all products it will choose first 6 of them
    page = request.GET.get('page') # This will get page number from url of browser.
    paged_products = paginator.get_page(page)
    all_products_count = all_products.count()
    context = {
        'all_products':paged_products,
        'all_products_count':all_products_count
    }
    return render(request, 'store/storehomepage.html',context)

def DetailProductPage(request, category_slug = None, product_id = None):
    if product_id and category_slug:
        product = ProductModel.objects.get(product_category__category_slug = category_slug, id = product_id)
        color_variations = VariationModel.objects.filter(product_id = product_id, variation_category = 'color', is_active = True)
        size_variations = VariationModel.objects.filter(product_id = product_id, variation_category = 'size',is_active = True)
        out_of_stock = False
        if product.product_stock <=0:
            out_of_stock =True
        context = {
            'product':product,
            'out_of_stock':out_of_stock,
            'color_variations':color_variations,
            'size_variations':size_variations,
        }
        return render(request, 'store/detail_product.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        searched_products = ProductModel.objects.filter(Q(product_description__icontains = keyword) | Q(product_name__icontains = keyword))
        context = {
            'all_products':searched_products
        }
    return render(request, 'store/storehomepage.html',context)