# Create your views here.
from django.shortcuts import render, redirect
from .models import Cita
from .form import MascotaForm, CitaForm

def lista_citas(vistas_request):
    citas = Cita.objects.all().order_by('fecha', 'hora')
    return render(vistas_request, 'gestion/lista_citas.html', {'citas': citas})

def registrar_paciente(vistas_request):
    if vistas_request.method == 'POST':
        mascota_form = MascotaForm(vistas_request.POST)
        cita_form = CitaForm(vistas_request.POST)
        if mascota_form.is_valid() and cita_form.is_valid():
            mascota_form.save()
            cita_form.save()
            return redirect('lista_citas')
    else:
        mascota_form = MascotaForm()
        cita_form = CitaForm()
    
    return render(vistas_request, 'gestion/registrar.html', {
        'mascota_form': mascota_form,
        'cita_form': cita_form
    })