import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from gestion.models import Mascota, Cita

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write('Generando datos ficticios...')

        nombres_mascotas = ['Firulais', 'Luna', 'Max', 'Bella', 'Thor', 'Mila', 'Rocky', 'Simba', 'Nala', 'Zeus', 
                            'Coco', 'Lola', 'Lucas', 'Kira', 'Bruno', 'Mia', 'Cooper', 'Pancho', 'Sasha', 'Toby']
        especies = ['Perro', 'Gato']
        razas = ['Mestizo', 'Golden Retriever', 'Siamés', 'Bulldog', 'Persa', 'Pastor Alemán', 'Poodle', 'Boxer']
        duenos = ['Carlos Pérez', 'María Gómez', 'Juan Silva', 'Ana Torres', 'Pedro Rojas', 'Sofía Morales', 
                  'Luis Díaz', 'Carmen Soto', 'Jorge Mendoza', 'Lucía Paredes']
        motivos = [
            'Control de vacunas anuales', 
            'Dolor estomacal y decaimiento', 
            'Revisión por picadura de pulgas', 
            'Corte de uñas y limpieza de oídos', 
            'Control post-operatorio', 
            'Tos persistente', 
            'Chequeo general preventivo'
        ]
        estados = ['pendiente', 'atendida', 'cancelada']

        # Limpiar datos anteriores (opcional)
        Cita.objects.all().delete()
        Mascota.objects.all().delete()

        # Crear 20 mascotas y sus citas
        for i in range(20):
            nombre = nombres_mascotas[i]
            especie = random.choice(especies)
            raza = random.choice(razas)
            nombre_dueno = random.choice(duenos)

            mascota = Mascota.objects.create(
                nombre=nombre,
                especie=especie,
                raza=raza,
                nombre_dueno=nombre_dueno
            )

            # Generar fecha aleatoria entre los últimos 5 días y los próximos 5 días
            dias_offset = random.randint(-5, 5)
            fecha_cita = datetime.now().date() + timedelta(days=dias_offset)
            
            # Hora aleatoria entre las 09:00 y las 18:00
            hora_cita = f"{random.randint(9, 17):02d}:{random.choice([0, 15, 30, 45]):02d}:00"

            Cita.objects.create(
                mascota=mascota,
                fecha=fecha_cita,
                hora=hora_cita,
                motivo_consulta=random.choice(motivos),
                estado=random.choice(estados)
            )

        self.stdout.write(self.style.SUCCESS('¡Se han generado exitosamente 20 pacientes y citas iniciales!'))