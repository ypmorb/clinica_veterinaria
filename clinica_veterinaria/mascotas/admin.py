from django.contrib import admin

from .models import Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'especie',
        'edad',
        'estado_vacunacion',
        'fecha_actualizacion',
    )

    list_filter = (
        'especie',
        'estado_vacunacion',
    )

    search_fields = (
        'nombre',
    )

    list_per_page = 20
