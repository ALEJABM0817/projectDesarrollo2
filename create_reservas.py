import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocrud.settings")

import django
django.setup()

from tasks.models import Reservas

def create_reservas(titulo, usuario, servicios, eventos,
                    alimentos, cantidad_personas, fecha_reserva):
    reservacion = Reservas(titulo=titulo, usuario = usuario, 
                           servicios = servicios, eventos = eventos,
                    alimentos = alimentos, cantidad_personas = cantidad_personas,
                      fecha_reserva = fecha_reserva)
    reservacion.save()
    print(f"reservación {titulo} creado correctamente.")

if __name__ == "__main__":
    create_reservas("Cumpleaños ana","ana", "DJ Hora Loca Meseros", "Cumpleaños",
                    "Comida Rápida1 Gaseosa Licor", "50", "2023-06-07")
    create_reservas("Cena Ejecutiva","maria", "Utilería Meseros", "Ejecutivos",
                    "Plato2 Jugo", "30", "2023-06-30")
    create_reservas("Quinces Lina","ryan", "DJ Utilería Hora Loca Meseros Decoración Bar", "Quinceaños",
                    "Plato1 Gaseosa Licor", "130", "2023-06-28")
    create_reservas("Graduación 2023","Camil", "DJ Hora Loca Meseros Decoración Bar", "Grados",
                    "Comida Rápida2 Licor Gaseosa", "80", "2023-06-29")

