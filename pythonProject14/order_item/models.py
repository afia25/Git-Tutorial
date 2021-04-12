from django.db import models
from customer.models import Customer
from product.models import Product

#from order_item.models import Sales
class Order_item(models.Model):
    invoice_id = models.TextField(primary_key=True)
    quantity = models.IntegerField()
    selling_price = models.IntegerField()
    discount = models.IntegerField()
    delivary_charge = models.IntegerField()
    transport_cost = models.IntegerField()
    total_price = models.IntegerField()
    payment=models.IntegerField()
    due=models.IntegerField()
    user_id=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product_id=models.ForeignKey(Product ,null=True,on_delete=models.SET_NULL)
    #invoice_id=models.ForeignKey(Sales,on_delete=models.CASCADE)

#from customer.models import Customer
#from product.models import Product
#class Sales(models.Model):
    #invoice_id = models.TextField(primary_key=True)
    #sales = models.IntegerField()
    #customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    #product_id=models.ForeignKey(Product ,on_delete=models.CASCADE)
