from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from tasks.models import Servicio
from tasks.models import Eventos
from tasks.models import Alimentos
from .forms import RegisterUserForm

# Create your views here.
def home (request):
 return render(request, 'home.html')

def signup(request):
 
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': RegisterUserForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'],
                )
                user.save()
                login(request, user)
                return redirect('selector')
            except IntegrityError:
                return render(request, 'signup.html', {
                'form': RegisterUserForm,
                 "error": 'El usuario ya existe'
            })
    return render(request, 'signup.html', {
        'form': RegisterUserForm,
        "error": 'Las contraseñas no coinciden'
            })

def tasks(request):
    return render(request, 'tasks.html')      

def cerrarS(request):
    logout(request)
    return redirect ('home') 
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
        'form': AuthenticationForm
    })
    else:
        user=authenticate(
        request, username=request.POST['username'],
             password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
        'form': AuthenticationForm,
        'error':'Usuario o contraseña incorrecta'
    })
        else:
            login(request, user)
            return redirect ('selector')
        
def selector(request):
    servicios = Servicio.objects.all()
    servicios_dj = Servicio.objects.filter(nombre='DJ')
    servicios_decoracion = Servicio.objects.filter(nombre='Decoración')
    servicios_hora_loca = Servicio.objects.filter(nombre='Hora Loca')
    servicios_utileria = Servicio.objects.filter(nombre='Utilería')
    servicios_meseros = Servicio.objects.filter(nombre='Meseros')
    servicios_bar = Servicio.objects.filter(nombre='Bar')
    total_servicios = 0
    
    eventos = Eventos.objects.all()
    eventos_c = Eventos.objects.filter(nombre='Cumpleaños')
    eventos_ba = Eventos.objects.filter(nombre='Bautizos')
    eventos_q = Eventos.objects.filter(nombre='Quinceaños')
    eventos_bo = Eventos.objects.filter(nombre='Bodas')
    eventos_fi = Eventos.objects.filter(nombre='Fiestas Infantiles')
    eventos_g = Eventos.objects.filter(nombre='Grados')
    eventos_e = Eventos.objects.filter(nombre='Ejecutivos')
    total_eventos = 0
    
    alimentos = Alimentos.objects.all()
    alimentos_e1 = Alimentos.objects.filter(nombre='Plato1')
    alimentos_e2 = Alimentos.objects.filter(nombre='Plato2')
    alimentos_c1 = Alimentos.objects.filter(nombre='Comida Rápida1')
    alimentos_c2 = Alimentos.objects.filter(nombre='Comida Rápida2')
    alimentos_j1 = Alimentos.objects.filter(nombre='Jugo')
    alimentos_l = Alimentos.objects.filter(nombre='Limonada')
    alimentos_g = Alimentos.objects.filter(nombre='Gaseosa')
    alimentos_l2 = Alimentos.objects.filter(nombre='Licores')
    alimentos_s = Alimentos.objects.filter(nombre='Snacks')
    total_alimentos = 0
    if request.method == 'POST':
        servicios_seleccionados = request.POST.getlist('servicios')
        eventos_seleccionados = request.POST.getlist('eventos')
        alimentos_seleccionados = request.POST.getlist('alimentos')
        for servicio_id in servicios_seleccionados:
            servicio = Servicio.objects.get(pk=servicio_id)
            total_servicios += servicio.precio
        
        for evento_id in eventos_seleccionados:
            evento = Eventos.objects.get(pk=evento_id)
            total_eventos += evento.precio
        
        for alimentos_id in alimentos_seleccionados:
            alimentos = Alimentos.objects.get(pk=alimentos_id)
            total_alimentos += alimentos.precio
    cantidad_personas = int(request.POST.get('Personas', 10))
    total_alimentos *= cantidad_personas
    total_general = str(total_servicios + total_eventos + total_alimentos)
    
    context = {
        'servicios': servicios,
        'servicios_dj': servicios_dj,
        'servicios_decoracion': servicios_decoracion,
        'servicios_hora_loca': servicios_hora_loca,
        'servicios_utileria': servicios_utileria,
        'servicios_meseros': servicios_meseros,
        'servicios_bar': servicios_bar,
        'eventos': eventos,
        'eventos_c': eventos_c,
        'eventos_ba': eventos_ba,
        'eventos_q': eventos_q,
        'eventos_bo': eventos_bo,
        'eventos_fi': eventos_fi,
        'eventos_g': eventos_g,
        'eventos_e': eventos_e,
        'alimentos_e1': alimentos_e1,
        'alimentos_e2': alimentos_e2,
        'alimentos_c1': alimentos_c1,
        'alimentos_c2': alimentos_c2,
        'alimentos_j1': alimentos_j1,
        'alimentos_l': alimentos_l,
        'alimentos_g': alimentos_g,
        'alimentos_l2': alimentos_l2,
        'alimentos_s': alimentos_s,
        'total_alimentos': total_alimentos,
        'total_servicios': total_servicios,
        'total_eventos': total_eventos,
        'total_general': total_general
    }
#--------------------------------------------------------------------------------------------------------------------
    
    return render(request, 'tasks.html', context)


