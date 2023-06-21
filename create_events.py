import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocrud.settings")

import django
django.setup()

from tasks.models import Eventos

def create_events(nombre, precio):
    eventos = Eventos(nombre=nombre, precio=precio)
    eventos.save()
    print(f"Evento {nombre} creado correctamente.")

if __name__ == "__main__":
    create_events("Cumpleaños", 100.0)
    create_events("Bautizos", 100.0)
    create_events("Quinceaños", 150.0)
    create_events("Bodas", 200.0)
    create_events("Fiestas Infantiles", 250.0)
    create_events("Grados", 80.0)
    create_events("Ejecutivos", 80.0)