# Generated by Django 4.1.7 on 2023-02-28 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_order_price_alter_customer_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='amount',
        ),
    ]
