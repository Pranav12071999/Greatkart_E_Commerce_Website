from .models import *

def category_links(request):
    all_categories = CategoryModel.objects.all()
    return dict(all_categories = all_categories)