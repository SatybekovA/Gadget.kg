from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField('Расположение', max_length= 100)

    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.CharField(max_length=50, null=True, blank=True, verbose_name='Цена')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'