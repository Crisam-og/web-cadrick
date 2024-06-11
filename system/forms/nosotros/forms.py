from django.forms import *
from system.models import *



class NosotrosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    class Meta:
        model = Nosotros
        fields = '__all__'
        #labels = {
        #    'title': 'Nombre',
        #    'description': 'Descripción',
        #}
        
        widgets = {      
            'historia': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una historia', 
                    'rows': 7,
                    'cols': 7 
                    }
                ),
            'mision': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una mision', 
                    'rows': 3,
                    'cols': 3 
                    }
                ),
             'vision': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una vision', 
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