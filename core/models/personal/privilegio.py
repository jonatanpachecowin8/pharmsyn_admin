from django.db import models

class Privilegio(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'privilegios'