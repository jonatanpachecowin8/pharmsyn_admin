from django.db import models
from core.models import Rol, Privilegio

class RolPrivilegio(models.Model):
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    privilegio = models.ForeignKey(Privilegio, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rol', 'privilegio')
        db_table = 'rol_privilegios'
        
    def __str__(self):
        return f"{self.rol.nombre} - {self.privilegio.nombre}"
    
    