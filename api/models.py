from django.db import models
import uuid

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=255, default = 'uncategorized')
    price = models.DecimalField(max_digits=7, decimal_places=2 )
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Order (models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.product} - {self.total_price}"