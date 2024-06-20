from django.forms import *
from system.models import *


class ServiciosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Servicios
        fields = '__all__'
        
        widgets = {
            'nombre_servicio': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del servicio',
                    
                    }
                ),
            'descripcion_servicio': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción', 
                    'rows': 3,
                    'cols': 3 
                    }
                ),
            'servicio_id': Select(
                attrs={
                    'class': 'form-control col-3',
                    'style': 'width: 100%'
                    }
                ),
            'imagen': FileInput(
                attrs={
                'class': 'form-control-file',
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