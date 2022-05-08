from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Persona, Apertura



def inicio(request):
    return render(request, "Personas/index.html")

def persona(request):
    persona = Persona(nombre="Garry", apellido="Kasparov",nacionalidad="Azerbaijan/URSS", ranking="2851")
    # persona.save()
    documento=f"Se ha cargado a correctamente {persona.nombre} {persona.apellido}"
    return render(request, "Personas/jugadores.html")

def apertura(request):
    apertura= Apertura(ecoCode="E01", nombre="Defensa Holandesa",ordenJugadas="1.d4 f5")
    # apertura.save()
    documento=f"Se ha cargado con éxito {apertura.nombre} en la base de datos"
    return render(request,"Personas/aperturas.html")

def nosotros(request):
    return render(request, "Personas/nosotros.html")