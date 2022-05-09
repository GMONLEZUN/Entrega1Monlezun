from django.http import Http404, HttpResponse
from django.shortcuts import render

from Personas.forms import PersonaFormulario
from .models import Persona, Apertura



def inicio(request):
    return render(request, "Personas/index.html")

def apertura(request):
    apertura= Apertura(ecoCode="E01", nombre="Defensa Holandesa",ordenJugadas="1.d4 f5")
    # apertura.save()
    documento=f"Se ha cargado con éxito {apertura.nombre} en la base de datos"
    return render(request,"Personas/aperturas.html")

def nosotros(request):
    return render(request, "Personas/nosotros.html")

def persona(request):
    jugadores = Persona.objects.all()
    if request.method == 'POST':
        formularioPersona = PersonaFormulario(request.POST)
        print(formularioPersona)
        if formularioPersona.is_valid():
            informacion = formularioPersona.cleaned_data
            persona = Persona(nombre=informacion['nombre'], apellido=informacion['apellido'], nacionalidad=informacion['nacionalidad'], ranking=informacion['ranking'])
            persona.save()
            return render(request, "Personas/persona.html", {"jugadores":jugadores}) #agregar un gracias por cargar
    else:
        formularioPersona = PersonaFormulario()

    return render(request, "Personas/persona.html", {"formularioPersona":formularioPersona, "jugadores":jugadores})

def buscar(request):
    if request.GET["apellido"]:
        apellido = request.GET["apellido"]
        jugadores = Persona.objects.filter(apellido__icontains=apellido)
        return render(request,"Personas/resultadosBusqueda.html", {"jugadores":jugadores})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def buscaPais(request):
    if request.GET["nacionalidad"]:
        nacionalidad = request.GET["nacionalidad"]
        jugadores = Persona.objects.filter(nacionalidad__icontains=nacionalidad)
        return render(request,"Personas/resultadosBusqueda.html", {"jugadores":jugadores})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def buscaNombre(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        jugadores = Persona.objects.filter(nombre__icontains=nombre)
        return render(request,"Personas/resultadosBusqueda.html", {"jugadores":jugadores})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)
