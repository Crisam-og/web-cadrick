from django.forms import *
from system.models import *


class ConfigForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Configuraciones
        fields = '__all__'
        exclude = ['nombre_config']
        
        widgets = {
            'nombre_config': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de configuracion',
                    'disabled': True,
                    'required':False,
                    
                    }
                ),
            'valor': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el valor',
                    
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