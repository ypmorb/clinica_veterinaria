from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'nombre',
            'especie',
            'edad',
            'estado_vacunacion',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la mascota'
            }),

            'especie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Perro, Gato, Conejo'
            }),

            'edad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),

            'estado_vacunacion': forms.Select(attrs={
                'class': 'form-select'
            }),
        }