from django.shortcuts import render
from tasks.models import reservas

def calendarioU(request):
    return render(request, 'fullcalendar.html')

def listarReservas(request):
    Reservas = reservas.objects.all()
    return render(request, "fullcalendar.html", {"reservas": Reservas})

def prueba(request):
    Reservas = reservas.objects.all()
    return render(request, "prueba.html", {'reservas': Reservas})