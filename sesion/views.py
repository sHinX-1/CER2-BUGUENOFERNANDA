from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Mascota, Especie

# Create your views here.
# INICIO, SOBRE NOSOTROS, MASCOTAS Y REGISTRO

def inicio(request):
    return render(request, 'sesion/inicio.html')

def nosotros(request):
    return render(request, 'sesion/nosotros.html')

def mascotas(request):
    lista_mascotas = Mascota.objects.all()
    especies = Especie.objects.all()

    especie_seleccionada = request.GET.get('especie')

    if especie_seleccionada:
        lista_mascotas = lista_mascotas.filter(especie__nombre=especie_seleccionada)

    return render(request, 'sesion/mascotas.html', {
        'mascotas': lista_mascotas,
        'especies': especies,
        'especie_seleccionada': especie_seleccionada})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')

    else:
        form = UserCreationForm()

    return render(request, 'sesion/registro.html', {'form': form})
