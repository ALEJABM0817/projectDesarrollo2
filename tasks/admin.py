from django.contrib import admin
from .models import Servicio
from .models import Eventos
from .models import Alimentos
from .models import reservas

admin.site.register(Servicio)
admin.site.register(Eventos)
admin.site.register(Alimentos)
admin.site.register(reservas)
