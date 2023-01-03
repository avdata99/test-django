from django.contrib import admin
from caballos.models import Caballo


@admin.register(Caballo)
class CaballoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "edad", "fecha_nacimiento", "anio_muerte"]
    list_filter = ["edad"]

