from django.db import models
from product .models import Product
class Supplier(models.Model):
    sup_id = models.TextField(primary_key=True)
    sup_name = models.CharField(max_length=50)
    sup_email = models.CharField(max_length=50)
    sup_contact=models.CharField(max_length=11)
    product_id=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
