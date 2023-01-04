from django.contrib import admin
from jinetes.models import Equitacion, Jinete


@admin.register(Jinete)
class JineteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento')


@admin.register(Equitacion)
class EquitacionAdmin(admin.ModelAdmin):
    list_display = ('jinete', 'caballo')
