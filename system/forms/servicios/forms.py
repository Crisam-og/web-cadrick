from django.forms import *
from system.models import *
from system.validators.formatChecker import *


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
            # 'imagen': FileInput(
            #     attrs={
            #     'class': 'form-control-file',
            #         }
            #     ),
        }
        
class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
      
class ImagenServiciosForm(ModelForm):
    imagen = MultipleFileField(label='Selecciona Imagenes del servicio', required=False, validators=[file_size, file_extension])

    class Meta:
        model = ImagenServicios
        fields = ['imagen']
        
            
    # def save(self, commit=True):
    #     data = {}
    #     form = super()
    #     try:
    #         if form.is_valid():
    #             form.save()
    #         else:
    #             data['error'] = form.errors
    #     except Exception as e:
    #         data['error'] = str(e)
    #     return data