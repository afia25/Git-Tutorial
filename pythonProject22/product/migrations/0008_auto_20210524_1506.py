# Generated by Django 3.1.7 on 2021-05-24 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_invoice_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='invoice_id',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='payment_status',
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='prod_id',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
