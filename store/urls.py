from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.StoreHomepage, name = 'StoreHomepage'),
    path('<slug:category_slug>/<int:product_id>', views.DetailProductPage, name = 'DetailProductPage'),
    path('<slug:category_slug>', views.StoreHomepage, name = 'sort_by_category'),
    

]