from django.db import models
from markets.models import Location, Product
# Create your models here.



GENDER_CHOICES = (
    ('MAN', 'Man'),
    ('WOMAN', 'Woman'),
    ('BI', 'Bi'),
    ('OTHER', 'Other')
)


class Customer(models.Model):
    name = models.CharField( max_length=225, null=True, blank=True, verbose_name='Customer name')
    age = models.IntegerField()
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='OTHER')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
    

class Employee(models.Model):
    name = models.CharField('Имя',max_length=50)
    age = models.IntegerField('Возраст')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='OTHER')    
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employer'
    
class Order(models.Model):
    order = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Заказ')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'