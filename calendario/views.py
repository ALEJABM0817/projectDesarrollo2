from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

def calendarioU(request):
    return render(request, 'fullcalendar.html')