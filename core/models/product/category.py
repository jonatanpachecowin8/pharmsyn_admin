from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=20)  # e.g., gr, lt

    def __str__(self):
        return self.name
