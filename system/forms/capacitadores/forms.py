from django.forms import *
from system.models import *
from django_summernote.widgets import SummernoteWidget

class CapacitadorForm(ModelForm):
    class Meta:
        model = Capacitador
        fields = ('nombre_capacitador','apellidos_capacitador','grado_academico','correo','descripcion_c','imagen')
        
        widgets = {
            'nombre_capacitador': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del capacitador'
                }
            ),
            'apellidos_capacitador': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el apellido del capacitador'
                }
            ),
            
            'grado_academico': Select(
                attrs = {
                    'class': 'form-control col-sm-2 control-label',
                    'placeholder': 'Ingrese el grado academico del capacitador'
                }
            ),
            
            'correo': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo del capacitador',
                }
            ),
            'descripcion_c': SummernoteWidget(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                    
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