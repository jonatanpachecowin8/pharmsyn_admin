from django.db import models
from core.models.cliente.user import User
from core.models.personal.branch import Branch

class Order(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField()
    payment_method = models.CharField(max_length=50)
    address = models.JSONField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"

    class Meta:
        db_table = 'core_order'
