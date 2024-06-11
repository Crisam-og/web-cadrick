from django.forms import *
from system.models import *


class EquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Equipo
        fields = '__all__'
        
        widgets = {
            'nombre_equipo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre',
                    
                    }
                ),
            'apellido_equipo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido',
                    
                    }
                ),
            'cargo': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el cargo',
                    
                    }
                ),
            'descripcion': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                    'rows': 3,
                    'cols': 3
                    
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