from django import views
from django.urls import path
from Personas.views import inicio,persona,apertura,nosotros


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('jugadores', persona, name="Jugadores"),
    path('aperturas', apertura, name="Aperturas"),
    path('nosotros', nosotros, name="Contacto"),
]