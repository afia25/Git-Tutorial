from django.db import models

class Inventory_admin(models.Model):
    inv_admin_id = models.TextField(primary_key=True)
    inv_admin_name = models.CharField(max_length=50)
    inv_admin_email = models.CharField(max_length=50)
