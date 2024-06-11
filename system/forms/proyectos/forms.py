from django.forms import *
from system.models import *


class ProyectoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Proyectos
        fields = '__all__'
        
        widgets = {
            'nombre_proyecto': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del proyecto',
                    
                    }
                ),
            'descripcion_corta': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion, Max: 240 caracteres',
                    'rows': 3,
                    'cols': 3
                    
                    }
                ),
            'descripcion_detallada': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion, Max: 240 caracteres',
                    'rows': 3,
                    'cols': 3
                    
                    }
                ),
            'fecha_de_proyecto': DateInput(
                attrs = {
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'cliente': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del proyecto',
                    
                    }
                ),
        }
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data