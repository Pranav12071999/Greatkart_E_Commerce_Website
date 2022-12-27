from django.db import models
from category.models import *
# Create your models here.
class ProductModel(models.Model):
    product_name                = models.CharField(max_length = 100, unique = True)
    product_slug                = models.SlugField(max_length = 100, unique = True)
    product_description         = models.TextField(blank = True)
    product_price               = models.IntegerField()
    product_image               = models.ImageField(upload_to = 'photoes/products')
    product_stock               = models.IntegerField()
    product_is_available        = models.BooleanField(default = True)
    product_category            = models.ForeignKey(CategoryModel, on_delete = models.CASCADE)
    product_created_date        = models.DateTimeField(auto_now_add = True)
    product_modified_date       = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = 'Product models'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.product_name
