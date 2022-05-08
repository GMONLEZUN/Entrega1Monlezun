from django import views
from django.urls import path
from Personas.views import inicio,persona,apertura,nosotros, buscar




urlpatterns = [
    path('', inicio, name="Inicio"),
    # path('jugadores', persona, name="Jugadores"),
    path('aperturas', apertura, name="Aperturas"),
    path('nosotros', nosotros, name="Contacto"),
    path('persona', persona, name="Persona"),
    # path('busquedaPersona', busquedaPersona, name="busquedaPersona"),
    path('buscar', buscar, name="buscar"),
]