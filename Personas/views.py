from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Persona, Apertura

def persona(self):
    persona = Persona(nombre="Garry", apellido="Kasparov",nacionalidad="Azerbaijan/URSS", ranking="2851")
    # persona.save()
    documento=f"Se ha cargado a correctamente {persona.nombre} {persona.apellido}"
    return HttpResponse(documento)

def apertura(self):
    apertura= Apertura(ecoCode="E01", nombre="Defensa Holandesa",ordenJugadas="1.d4 f5")
    # apertura.save()
    documento=f"Se ha cargado con éxito {apertura.nombre} en la base de datos"
    return HttpResponse(documento)
