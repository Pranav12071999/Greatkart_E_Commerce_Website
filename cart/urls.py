from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CartHomePage, name = 'CartHomePage'),
    path('add/<int:product_id>', views.add_cart, name = 'add_cart'),
    path('substract/<int:product_id>/<int:cart_item_id>', views.substract_cart_item, name = 'substract_cart_item'),
    path('remove/<int:product_id>/<int:cart_item_id>', views.remove_cart_item, name = 'remove_cart_item'),
    path('checkout/', views.checkout, name = 'checkout'),
]