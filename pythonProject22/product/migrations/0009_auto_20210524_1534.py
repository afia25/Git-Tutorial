# Generated by Django 3.1.7 on 2021-05-24 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20210524_1506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock_buying_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock_selling_price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='tracking_number',
        ),
        migrations.RemoveField(
            model_name='products',
            name='transaction_number',
        ),
    ]
