import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangocrud.settings")

import django
django.setup()

from tasks.models import Alimentos

def create_foods(nombre, precio):
    alimentos =Alimentos(nombre=nombre, precio=precio)
    alimentos.save()
    print(f"Alimento o Bebida {nombre} creado correctamente.")

if __name__ == "__main__":
    create_foods("Plato1", 100.0)
    create_foods("Plato2", 100.0)
    create_foods("Comida Rápida1", 50.0)
    create_foods("Comida Rápida2", 50.0)
    create_foods("Jugo", 20.0)
    create_foods("Limonada", 10.0)
    create_foods("Gaseosa", 50.0)
    create_foods("Licor", 300.0)
    create_foods("Snacks", 200.0)