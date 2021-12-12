from django.db import models

# Create your models here.

class Curso(models.Model):
    
    nombre = models.CharField(max_length=40)
    comision = models.IntegerField()


    def __str__(self) -> str:
        return (f"Nombre: {self.nombre} /// COMISION: {self.comision}" )
