import re
from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    nacionalidad=models.CharField(max_length=255)
    ranking=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Apertura(models.Model):
    ecoCode=models.CharField(max_length=40)
    nombre=models.CharField(max_length=255)
    ordenJugadas=models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre}"

class Torneo(models.Model):
    nombre=models.CharField(max_length=255)
    sitio=models.CharField(max_length=255)
    year=models.IntegerField()
    partidaN=models.IntegerField()
    humano=models.CharField(max_length=255)
    maquina=models.CharField(max_length=255)
    partidaR=models.CharField(max_length=10)
    ganador=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.nombre} {self.sitio} {self.year}"

class Campeones(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    periodo=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"