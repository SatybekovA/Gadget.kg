# Generated by Django 4.1.7 on 2023-02-28 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_customer_name_customer_customer_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='customer_name',
            new_name='name',
        ),
    ]
