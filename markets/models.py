from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField('Расположение', max_length= 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    price = models.IntegerField('цена')

    def __str__(self):
        return self.name