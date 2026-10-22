# Register your models here.
from django.contrib import admin
from .models import Mascota, Cita

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'nombre_dueno')
    search_fields = ('nombre', 'nombre_dueno', 'especie')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('mascota', 'fecha', 'hora', 'motivo_consulta', 'estado')
    list_filter = ('estado', 'fecha')  
    search_fields = ('mascota__nombre', 'motivo_consulta')

"""
Username: Clinica_Veterinaria
Email address: clinica_veterinaria@HuellasSanas.cl
Password: Clinica.123
"""