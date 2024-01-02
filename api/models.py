from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=255, default = 'uncategorized')
    price = models.DecimalField(max_digits=7, decimal_places=2 )
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Order (models.Model):
    pass