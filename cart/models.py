from django.db import models
from store.models import *
# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length = 250, blank = True)
    cart_date_added = models.DateField(auto_now_add = True)

    def __str__(self) -> str:
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(ProductModel, on_delete = models.CASCADE)
    variations = models.ManyToManyField(VariationModel,blank=True)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default = True)

    def sub_total(self):
        return self.product.product_price * self.quantity
    
    def get_url(self):
        return reverse('DetailProductPage', args=[self.product.product_category.category_slug, self.product.id])

    def __str__(self):
        return self.product.product_name