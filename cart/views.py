from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if cart is None:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = ProductModel.objects.get(id = product_id)
    variation_list = []
    if request.method == 'POST':
        for item in request.POST:
            key = item
            value = request.POST[key]
            try:
                variation = VariationModel.objects.get(product = product, variation_category__iexact = key, variation_value = value)
                variation_list.append(variation)
            except:
                pass
        
        # Fetching or creating cart
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save()
    # Fetching or creating cart item based on cart.
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user = request.user, product = product)
        else:
            cart_items = CartItem.objects.filter(cart = cart, product = product)
        if cart_items.exists():
            existing_variations_list = []
            index_list = []   
            for item in cart_items:
                existing_variation = item.variations.all()
                existing_variations_list.append(list(existing_variation))
                index_list.append(item.id)
            if variation_list in existing_variations_list:
                index = existing_variations_list.index(variation_list)
                cart_id = index_list[index]
                cart_item = CartItem.objects.get(id = cart_id)
                cart_item.quantity += 1
                if request.user.is_authenticated:
                    cart_item.user = request.user
                cart_item.save()
            else:
                cart_item = CartItem.objects.create(
                                cart = cart,
                                quantity = 1,
                                product = product)
                cart_item.variations.clear()
                if len(variation_list) > 0:
                    cart_item.variations.add(*variation_list)
                cart_item.save()
        else:
            if request.user.is_authenticated:
                cart_item = CartItem.objects.create(
                                user = request.user,
                                cart = cart,
                                quantity = 1,
                                product = product)
            else:
                cart_item = CartItem.objects.create(
                                    cart = cart,
                                    quantity = 1,
                                    product = product)
            cart_item.variations.clear()
            if len(variation_list) > 0:
                cart_item.variations.add(*variation_list)
            cart_item.save()

        # cart_item.quantity += 1
        # cart_item.save()
    except CartItem.DoesNotExist:
        if request.user.is_authenticated:
                cart_item = CartItem.objects.create(
                                user = request.user,
                                cart = cart,
                                quantity = 1,
                                product = product)
        else:
            cart_item = CartItem.objects.create(
                cart = cart,
                quantity = 1,
                product = product
            )
        cart_item.variations.clear()
        if len(variation_list) > 0:
            cart_item.variations.add(*variation_list)
        cart_item.save()
    return redirect('CartHomePage')

def CartHomePage(request, cart_items = None):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user = request.user, is_active = True)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_items = CartItem.objects.filter(cart = cart, is_active = True)
        total = 0
        tax = 0
        grand_total = 0
        for cart_item in cart_items:
            total += total + cart_item.product.product_price * cart_item.quantity
        tax = int(0.2 * total)
        grand_total = total + tax
        context = {
            'total':total,
            'tax':tax,
            'grand_total':grand_total,
            'cart_items':cart_items
        }
    except Cart.DoesNotExist or CartItem.DoesNotExist:
        context = {}
    return render(request, 'cart/carthomepage.html',context)


def substract_cart_item(request, product_id, cart_item_id):
    product = ProductModel.objects.get(id = product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(id = cart_item_id, user = request.user, product = product)
        else:
            cart_item = CartItem.objects.get(id = cart_item_id, cart = cart, product = product)
        if cart_item.quantity == 1:
            cart_item.delete()
        else:
            cart_item.quantity -= 1
        cart_item.save()
        return redirect('CartHomePage')
    except:
        pass

def remove_cart_item(request, product_id, cart_item_id):
    product = ProductModel.objects.get(id = product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_item = CartItem.objects.get(id = cart_item_id, cart = cart, product = product)
        cart_item.delete()
        return redirect('CartHomePage')
    except:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(id = cart_item_id, user = request.user, product = product)
            cart_item.delete()
            return redirect('CartHomePage')
@login_required(login_url='login')
def checkout(request):
    try:
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user = request.user, is_active = True)
        else:
            cart = Cart.objects.get(cart_id = _cart_id(request))
            cart_items = CartItem.objects.filter(cart = cart, is_active = True)
        total = 0
        tax = 0
        grand_total = 0
        for cart_item in cart_items:
            total += total + cart_item.product.product_price * cart_item.quantity
        tax = int(0.2 * total)
        grand_total = total + tax
        context = {
            'total':total,
            'tax':tax,
            'grand_total':grand_total,
            'cart_items':cart_items
        }
    except Cart.DoesNotExist or CartItem.DoesNotExist:
        context = {}
    return render(request, 'cart/checkout.html',context)