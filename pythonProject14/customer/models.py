from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user_id = models.TextField(primary_key=True)
    user_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)

class UserDetails(models.Model):
    name = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=150)
    delivery_within_what_time=models.CharField(max_length=150)
    alternative_contact_name = models.CharField(max_length=150)
    alternative_contact_number = models.CharField(max_length=150)
    payment_method=models.CharField(max_length=150)

class Payment(models.Model):
    payment_method = models.TextField()
    payment_status = models.TextField()
    #due_payment = models.IntegerField()
    user_id = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)


class User_Details(models.Model):
    name = models.CharField(max_length=30)
    delivary_address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=150)
    delivery_within_what_time=models.CharField(max_length=150)
    alternative_contact_name = models.CharField(max_length=150)
    alternative_contact_number = models.CharField(max_length=150)
    payment_method=models.CharField(max_length=150)

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about = models.CharField(max_length=150,blank=True)
    profile_picture=models.ImageField(default='default.jpg',upload_to='profile_pictures')
    user_type=models.CharField(max_length=16,default='')
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user_type=models.CharField(max_length=16,default='')
    def __str__(self):
        return self.user.username



