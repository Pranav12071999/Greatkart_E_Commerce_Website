from .models import *
from .views import _cart_id
def counter(request):
    cart_count = 0
    # This is used when we are under admin panel then it should show the null dictionary 
    if 'admin' in request.path:
        return {}
    else:
        try:
            if request.user.is_authenticated:
                cart_items = CartItem.objects.filter(user = request.user)
            else:
                cart = Cart.objects.filter(cart_id = _cart_id(request))
                cart_items = CartItem.objects.filter(cart = cart[:1]) # Not understood why this slicing?
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count = cart_count)
