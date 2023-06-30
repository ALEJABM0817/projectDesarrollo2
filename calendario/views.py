from django.shortcuts import render
from tasks.models import Reservas

def calendarioU(request):
    return render(request, 'fullcalendar.html')

def listarReservas(request):
    Reservas = Reservas.objects.all()
    return render(request, "fullcalendar.html", {"reservas": Reservas})

def prueba(request):
    Reservas = Reservas.objects.all()
    return render(request, "prueba.html", {'reservas': Reservas})