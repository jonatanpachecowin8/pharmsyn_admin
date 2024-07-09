from django.db import models

class Laboratory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    is_featured = models.BooleanField(default=False)
    product_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name