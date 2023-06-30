from django.contrib.auth.models import User
from django.db import models

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class Eventos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

class Alimentos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)



class Reservas(models.Model):
    titulo = models.CharField(max_length=1000)
    usuario = models.CharField(max_length=100)
    servicios = models.CharField(max_length=100)
    eventos = models.CharField(max_length=100)
    alimentos = models.CharField(max_length=100)
    cantidad_personas = models.DecimalField(max_digits=3, decimal_places=0)
    fecha_reserva = models.DateField()