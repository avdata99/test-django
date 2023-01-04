from django.db import models


class Caballo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)
    anio_muerte = models.IntegerField(null=True, blank=True)
    datos_generales = models.JSONField(null=True, blank=True)

    edad = models.IntegerField(default=10)
    jinete_principal = models.ForeignKey(
        'jinetes.Jinete',
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return f'CBL {self.nombre}'
