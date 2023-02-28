# Generated by Django 4.1.7 on 2023-02-27 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employer',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Gender',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('client_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.customer')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.employee')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Заказ', to='markets.product')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.gender'),
        ),
        migrations.AddField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.location'),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.gender'),
        ),
        migrations.AddField(
            model_name='customer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.location'),
        ),
    ]