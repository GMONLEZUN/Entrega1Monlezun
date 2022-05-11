from django import views
from django.urls import path
from Personas.views import inicio,persona,nosotros, buscar, buscaNombre, buscaPais, torneo, buscarTorneoY, buscarTorneoJ, buscarTorneoN, campeones




urlpatterns = [
    path('', inicio, name="Inicio"),
    path('campeones', campeones, name="Campeones"),
    path('nosotros', nosotros, name="Contacto"),
    path('persona', persona, name="Persona"),
    path('buscar', buscar, name="buscar"),
    path('buscaNombre', buscaNombre, name="buscaNombre"),
    path('buscaPais', buscaPais, name="buscaPais"),
    path('BuscartorneoY', buscarTorneoY, name="buscarTorneoY"),
    path('BuscartorneoN', buscarTorneoN, name="buscarTorneoN"),
    path('BuscartorneoJ', buscarTorneoJ, name="buscarTorneoJ"),
    path('torneo', torneo, name="Torneo"),
]