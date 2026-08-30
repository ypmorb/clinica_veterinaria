from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.lista_mascotas,
        name='lista_mascotas'
    ),

    path(
        'pendientes/',
        views.mascotas_pendientes,
        name='mascotas_pendientes'
    ),

    path(
        'crear/',
        views.crear_mascota,
        name='crear_mascota'
    ),

    path(
        'editar/<int:id>/',
        views.editar_mascota,
        name='editar_mascota'
    ),

    path(
        'eliminar/<int:id>/',
        views.eliminar_mascota,
        name='eliminar_mascota'
    ),
]