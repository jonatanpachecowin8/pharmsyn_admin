from django.db import models
from core.models.personal.branch import Branch
from core.models.product.product import Product

class ProductVariation(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variations')
    image = models.URLField()
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    attribute_values = models.JSONField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Assuming this is the branch where this variation is located

    def __str__(self):
        return f"{self.sku.title} - {self.description}"
