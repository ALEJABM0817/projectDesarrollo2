import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocrud.settings")

import django
django.setup()

from tasks.models import reservas

def create_reservas(titulo, fecha):
    reservacion = reservas(titulo=titulo, fecha=fecha)
    reservacion.save()
    print(f"reservación {titulo} creado correctamente.")

if __name__ == "__main__":
    create_reservas("Cumpleaños", "2023-06-07")
    create_reservas("Bautizo", "2023-06-27")
    create_reservas("Boda", "2023-06-14")
    create_reservas("Fiesta", "2023-06-30")
    create_reservas("Grado", "2023-06-28")
    create_reservas("Ejecutivo", "2023-06-01")
