from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Mascota
from .forms import MascotaForm


@login_required
def lista_mascotas(request):

    mascotas = Mascota.objects.all()

    nombre = request.GET.get('nombre', '')
    especie = request.GET.get('especie', '')

    if nombre:
        mascotas = mascotas.filter(nombre__icontains=nombre)

    if especie:
        mascotas = mascotas.filter(especie__iexact=especie)

    especies = (
        Mascota.objects
        .values_list('especie', flat=True)
        .distinct()
        .order_by('especie')
    )

    contexto = {
        'mascotas': mascotas,
        'especies': especies,
        'nombre': nombre,
        'especie_seleccionada': especie,
    }

    return render(
        request,
        'mascotas/lista.html',
        contexto
    )


@login_required
def mascotas_pendientes(request):

    mascotas = Mascota.objects.filter(
        estado_vacunacion='PENDIENTE'
    )

    return render(
        request,
        'mascotas/lista.html',
        {
            'mascotas': mascotas,
            'titulo': 'Mascotas con vacunas pendientes',
        }
    )


@login_required
def crear_mascota(request):

    if not request.user.is_staff:
        messages.error(
            request,
            'No tienes permisos para crear mascotas.'
        )
        return redirect('lista_mascotas')

    if request.method == 'POST':

        formulario = MascotaForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Mascota registrada correctamente.'
            )

            return redirect('lista_mascotas')

    else:
        formulario = MascotaForm()

    return render(
        request,
        'mascotas/formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Registrar mascota',
        }
    )


@login_required
def editar_mascota(request, id):

    if not request.user.is_staff:
        messages.error(
            request,
            'No tienes permisos para editar mascotas.'
        )
        return redirect('lista_mascotas')

    mascota = get_object_or_404(Mascota, id=id)

    if request.method == 'POST':

        formulario = MascotaForm(
            request.POST,
            instance=mascota
        )

        if formulario.is_valid():
            formulario.save()

            messages.success(
                request,
                'Mascota actualizada correctamente.'
            )

            return redirect('lista_mascotas')

    else:
        formulario = MascotaForm(instance=mascota)

    return render(
        request,
        'mascotas/formulario.html',
        {
            'formulario': formulario,
            'titulo': 'Editar mascota',
        }
    )


@login_required
def eliminar_mascota(request, id):

    if not request.user.is_staff:
        messages.error(
            request,
            'No tienes permisos para eliminar mascotas.'
        )
        return redirect('lista_mascotas')

    mascota = get_object_or_404(Mascota, id=id)

    if request.method == 'POST':
        mascota.delete()

        messages.success(
            request,
            'Mascota eliminada correctamente.'
        )

        return redirect('lista_mascotas')

    return render(
        request,
        'mascotas/confirmar_eliminar.html',
        {'mascota': mascota}
    )
