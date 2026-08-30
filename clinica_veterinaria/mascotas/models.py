from django.db import models

class Mascota(models.Model):

    ESTADOS_VACUNACION = [
        ('AL_DIA', 'Al día'),
        ('PENDIENTE', 'Pendiente'),
        ('ALERGIA', 'Alergia a vacunas'),
    ]

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
    estado_vacunacion = models.CharField(
        max_length=20,
        choices=ESTADOS_VACUNACION,
        default='PENDIENTE'
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def __str__(self):
        return self.nombre
