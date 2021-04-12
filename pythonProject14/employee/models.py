from django.db import models

class Employee(models.Model):
    employee_id = models.TextField(primary_key=True)
    employee_name = models.CharField(max_length=40)
    employee_phone = models.CharField(max_length=11)
    employee_email = models.CharField(max_length=30)

from employee.models import Employee
from product.models import Product
class Shipment(models.Model):
    shipment_date = models.TextField()
    tracking_number = models.CharField(max_length=15, primary_key=True)
    employee_id = models.ForeignKey(Employee,null=True,on_delete=models.SET_NULL)
    product_id=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)

