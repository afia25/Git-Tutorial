from django.db import models



class Products(models.Model):
    product_id=models.CharField(max_length=10)
    product_name=models.CharField(max_length=30,default='')
    category_name=models.CharField(max_length=30,default='')
    description=models.CharField(max_length=100,default='')
    buying_price=models.IntegerField(default=1)
    selling_price=models.IntegerField(default=1)
    purchase=models.IntegerField(default=1)
    sale=models.IntegerField(default=1)
    stock =models.IntegerField(default=1)
    stock_buying_price=models.IntegerField(default=1)
    stock_selling_price=models.IntegerField(default=1)
    transaction_number=models.TextField(default=1)
    tracking_number=models.TextField(default=1)
    #customer=models.ForeignKey(CustomerInfo, null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.product_name


    #supplier=models.ForeignKey(SupplierInfo, on_delete=models.SET_NULL)


class CustomerInfo(models.Model):
    user_id=models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=150)
    delivery_within_what_time=models.CharField(max_length=150)
    alternative_contact_name = models.CharField(max_length=150)
    alternative_contact_number = models.CharField(max_length=150)
    payment_method=models.CharField(max_length=150)
    profile_picture=models.ImageField(default='default.jpg',upload_to='profile_pictures')
    product= models.ForeignKey(Products,null=True,on_delete=models.SET_NULL,blank=True)

    quantity=models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    invoice_id = models.CharField(max_length=10)
    discount = models.IntegerField()
    delivery_charge = models.IntegerField()

    total_price = models.IntegerField()
    payment = models.IntegerField()
    due = models.IntegerField()
    payment_status = models.TextField()
    customer = models.ForeignKey(CustomerInfo,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products,null=True, on_delete=models.SET_NULL)
    quantity=models.IntegerField(default=0)










class Sales(models.Model):
    invoice = models.ForeignKey(Invoice,null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Products,null=True, on_delete=models.SET_NULL)
    pofit = models.IntegerField()
    customer = models.ForeignKey(CustomerInfo,null=True, on_delete=models.SET_NULL)




class SupplierInfo(models.Model):
    supplier_id=models.CharField(max_length=10)
    sup_name = models.CharField(max_length=50)
    sup_email = models.CharField(max_length=50)
    sup_contact=models.CharField(max_length=11)
    product=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    invoice = models.ForeignKey(Invoice, null=True,on_delete=models.SET_NULL)

    def __str__(self):
        return self.sup_name

class Order(models.Model):
    product_id=models.CharField(max_length=10)
    product_name=models.TextField()
    user_id =models.TextField()
    user_name=models.TextField()