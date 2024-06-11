from django.forms import *
from system.models import *
from django_summernote.widgets import SummernoteWidget

class IncripcionesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Inscripciones
        fields = '__all__'
        
        widgets = { 
            'nombre_ins': TextInput(attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Ingrese su nombre',
                'type': 'text',
            }),
            'apellidos_ins': TextInput(attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Ingrese su apellido',
                'type': 'text',
            }),
            'telefono': TextInput(attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Ingrese su numero de telefono',
                'type': 'text',
            }),
            'correo': TextInput(attrs={
                'class': 'form-control',
                'name': 'email',
                'placeholder': 'Ingrese su correo',
                'type': 'text',
            }),
            'profesion': TextInput(attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Ingrese su profesión',
                'type': 'text',
            }),
            'grado_academico': Select(attrs={
                'class': 'form-control',
                'placeholder':'Seleccione su grado academico',
            }),
            'curso_id': Select(attrs={
                'class': 'form-control',
                'placeholder':'Seleccione su grado academico',
            }),
             'consulta': Textarea(attrs={
                'class': 'form-control',
                'name':'comment',
                'placeholder':'Consulta*'
            }),
            
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