# Generated by Django 3.1.7 on 2021-05-22 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='customer_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.user_details'),
        ),
    ]
