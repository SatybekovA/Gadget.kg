from django.db import models
from markets.models import Location, Product
# Create your models here.



class Gender(models.Model):
    gender =  models.CharField( max_length=50, verbose_name='Gender')

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Gender'

class Customer(models.Model):
    name = models.CharField('Имя',max_length=50)
    age = models.IntegerField('Возраст')
    gender =  models.ForeignKey( Gender, on_delete=models.CASCADE )
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    

class Employee(models.Model):
    name = models.CharField('Имя',max_length=50)
    age = models.IntegerField('Возраст')
    gender =  models.ForeignKey(Gender, on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employer'
    
class Order(models.Model):
    order = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Заказ')
    client_link = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    
    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'