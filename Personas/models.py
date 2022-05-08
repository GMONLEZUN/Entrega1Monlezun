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