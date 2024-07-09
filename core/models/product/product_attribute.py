from django.db import models
from core.models.product.product import Product

class ProductAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=100)
    values = models.JSONField()

    def __str__(self):
        return f"{self.product.title} - {self.name}"