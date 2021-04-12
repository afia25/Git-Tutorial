from django.db import models
from product .models import Product

class Inventory(models.Model):
    inventoy_id = models.TextField(primary_key=True)
    barcode = models.IntegerField()
    product_id=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
from product .models import Product
class Category(models.Model):
    category_id = models.TextField(primary_key=True)
    category_name = models.CharField(max_length=50)
    product_id = models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)
