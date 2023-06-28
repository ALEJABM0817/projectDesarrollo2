from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from tasks.models import reservas

def calendarioU(request):
    return render(request, 'fullcalendar.html')

def listarReservas(request):
    Reservas = reservas.objects.all()
    return render(request, "fullcalendar.html", {"reservas": Reservas})