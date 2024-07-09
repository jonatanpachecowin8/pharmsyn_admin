from django.db import models
from core.models.personal.laboratory import Laboratory
from core.models.personal.personal import Personal
from core.models.product.category import Category

class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    title = models.CharField(max_length=200)
    thumbnail = models.URLField()
    product_type = models.CharField(max_length=50)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Personal, on_delete=models.SET_NULL, null=True, related_name='created_products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title