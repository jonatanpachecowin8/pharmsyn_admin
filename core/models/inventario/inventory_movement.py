from django.db import models
from core.models.personal.branch import Branch
from core.models.personal.personal import Personal
from core.models.product.product import Product

class InventoryMovement(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=20)  # e.g., 'in', 'out'
    timestamp = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, related_name='modified_inventory_movements')

    def __str__(self):
        return f"{self.product.title} - {self.quantity} ({self.movement_type})"
