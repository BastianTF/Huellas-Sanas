# Create your models here.
from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50) 
    raza = models.CharField(max_length=50)
    nombre_dueno = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - Dueño: {self.nombre_dueno}"

class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('atendida', 'Atendida'),
        ('cancelada', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    motivo_consulta = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Cita para {self.mascota.nombre} el {self.fecha} a las {self.hora} [{self.estado}]"