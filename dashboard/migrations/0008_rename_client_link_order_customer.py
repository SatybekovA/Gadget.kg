# Generated by Django 4.1.7 on 2023-02-28 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_rename_customer_name_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='client_link',
            new_name='customer',
        ),
    ]