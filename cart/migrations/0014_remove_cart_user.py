# Generated by Django 4.1.7 on 2023-04-04 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_cart_razorpay_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
