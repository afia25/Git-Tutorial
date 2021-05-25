# Generated by Django 3.1.7 on 2021-04-01 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_id',
            field=models.TextField(primary_key=True, serialize=False),
        ),
    ]