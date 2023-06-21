import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocrud.settings")

import django
django.setup()

from tasks.models import Servicio

def create_service(nombre, precio):
    servicio = Servicio(nombre=nombre, precio=precio)
    servicio.save()
    print(f"Servicio {nombre} creado correctamente.")

if __name__ == "__main__":
    create_service("DJ", 100.0)
    create_service("Hora Loca", 50.0)
    create_service("Utilería", 50.0)
    create_service("Decoración", 200.0)
    create_service("Meseros", 150.0)
    create_service("Bar", 80.0)
