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
    create_reservas("Bautizo","ana", "DJ Hora Loca Meseros", "Bautizo",
                    "Comida Rápida1 Gaseosa Licor", "50", "2023-06-15")
    create_reservas("ejecutivo","maria", "Utilería Meseros", "Ejecutivos",
                    "Plato2 Jugo", "30", "2023-06-01")
    create_reservas("Cumpleaños","ryan", "DJ Utilería Hora Loca Meseros Decoración Bar", "Cumpleaños",
                    "Plato1 Gaseosa Licor", "130", "2023-06-25")
    create_reservas("Quinceaños","Camil", "DJ Hora Loca Meseros Decoración Bar", "Quinceaños",
                    "Comida Rápida2 Licor Gaseosa", "80", "2023-06-03")
    create_reservas("Cumpleañoss","petro", "DJ Utilería Hora Loca Meseros Decoración Bar", "Cumpleaños",
                    "Plato2 Gaseosa Licor", "130", "2023-06-17")
    create_reservas("Bodas","Camil", "DJ Hora Loca Meseros Decoración Bar", "Grados",
                    "Comida Rápida2 Licor Gaseosa", "80", "2023-06-14")
    create_reservas("Fiesta","ryan", "DJ Utilería Hora Loca Bar", "Cumpleaños",
                    "Comida Rápida2 Gaseosa Licor", "130", "2023-06-20")
    create_reservas("Eventos","ana", "DJ Hora Loca Meseros Decoración Bar", "Grados",
                    "Comida Rápida2 Licor Gaseosa", "80", "2023-05-28")


