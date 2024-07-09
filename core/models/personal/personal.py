from django.db import models
from core.models import Rol

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    estado = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
    class Meta:
        db_table = 'personal'