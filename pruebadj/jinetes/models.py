from django.db import models


class Jinete(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'JNT {self.nombre} {self.apellido}'


class Equitacion(models.Model):
    jinete = models.ForeignKey(Jinete, on_delete=models.CASCADE)
    caballo = models.ForeignKey('caballos.Caballo', on_delete=models.CASCADE)
