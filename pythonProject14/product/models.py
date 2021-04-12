from django.db import models

class Product(models.Model):
    product_id = models.TextField()
    product_name = models.CharField(max_length=30)
    selling_price = models.IntegerField()
    buying_price = models.IntegerField()

from product .models import Product
class Storage(models.Model):
    stock_id = models.TextField(primary_key=True)
    stock = models.IntegerField()
    stock_buying_price = models.IntegerField()
    stock_selling_price = models.IntegerField()
    purchase = models.IntegerField()
    sales = models.IntegerField()
    product_id = models.ForeignKey(Product, null=True,on_delete=models.SET_NULL)