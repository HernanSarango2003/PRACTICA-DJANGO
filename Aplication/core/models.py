from django.db import models

# Create your models here.

class Doctor(models.Model):
    cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    estado = models.BooleanField(default=True, verbose_name="Estado Activo")

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"
        ordering = ['nombre']
