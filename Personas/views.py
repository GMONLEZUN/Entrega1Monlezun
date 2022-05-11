from django.http import HttpResponse
from django.shortcuts import render

from Personas.forms import PersonaFormulario, TorneoFormulario, CampeonesFormulario
from .models import Persona, Torneo, Campeones



def inicio(request):
    return render(request, "Personas/index.html")


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

def torneo(request):
    torneos = Torneo.objects.all()
    if request.method == 'POST':
        formularioTorneo = TorneoFormulario(request.POST)
        print(formularioTorneo)
        if formularioTorneo.is_valid():
            informacion = formularioTorneo.cleaned_data
            persona = Torneo(nombre=informacion['nombre'], sitio=informacion['sitio'], year=informacion['year'], partidaN=informacion['partidaN'], humano=informacion['humano'], maquina=informacion['maquina'], partidaR=informacion['partidaR'], ganador=informacion['ganador'])
            persona.save()
            return render(request, "Personas/torneo.html", {"torneos":torneos}) #agregar un gracias por cargar
    else:
        formularioTorneo = TorneoFormulario()

    return render(request, "Personas/torneo.html", {"formularioTorneo":formularioTorneo, "torneos":torneos})

def buscarTorneoY(request):
    if request.GET["year"]:
        year = request.GET["year"]
        torneos = Torneo.objects.filter(year__icontains=year)
        return render(request,"Personas/resultadosBusqueda.html", {"torneos":torneos})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def buscarTorneoN(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        torneos = Torneo.objects.filter(nombre__icontains=nombre)
        return render(request,"Personas/resultadosBusqueda.html", {"torneos":torneos})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)

def buscarTorneoJ(request):
    if request.GET["humano"]:
        humano = request.GET["humano"]
        torneos = Torneo.objects.filter(humano__icontains=humano)
        return render(request,"Personas/resultadosBusqueda.html", {"torneos":torneos})

    else:
        respuesta = "No enviaste datos"
        return HttpResponse(respuesta)


def campeones(request):
    campeones = Campeones.objects.all()
    if request.method == 'POST':
        formularioCampeones = CampeonesFormulario(request.POST)
        print(formularioCampeones)
        if formularioCampeones.is_valid():
            informacion = formularioCampeones.cleaned_data
            campeon = Campeones(nombre=informacion['nombre'], apellido=informacion['apellido'], periodo=informacion['periodo'])
            campeon.save()
            return render(request, "Personas/campeones.html", {"campeones":campeones}) #agregar un gracias por cargar
    else:
        formularioCampeones = CampeonesFormulario()

    return render(request, "Personas/campeones.html", {"formularioCampeones":formularioCampeones, "campeones":campeones})