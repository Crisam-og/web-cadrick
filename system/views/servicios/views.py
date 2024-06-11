from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from system.models import *
from system.forms.servicios.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from system.mixin import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ServicioListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    model = Servicios
    template_name = 'servicios/list.html'
    permission_required = 'view_servicios'
    #create_url = 'servicios/create.html'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de servicios'
        context['create_url'] = reverse_lazy('servicios_create')
        return context

class ServicioCreateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Servicios
    form_class = ServiciosForm 
    template_name = 'servicios/create.html' 
    success_url = reverse_lazy('servicios_list')
    permission_required = 'add_servicios'
    url_redirect = success_url
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No hay registros'
            
        except Exception as e:
            data['error'] = str(e)
            
        return JsonResponse(data) 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar nuevo servicio'
        context['entity'] = 'Servicios'
        context ['icon'] = 'fas fa-plus'
        context['list_url'] = reverse_lazy('servicios_list')
        context['action'] = 'add'

        return context
    
class ServicioUpdateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Servicios
    form_class = ServiciosForm
    template_name = 'servicios/create.html'
    success_url = reverse_lazy('servicios_list')
    permission_required = 'change_servicios'
    url_redirect = success_url
    
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                if form.is_valid():
                    form.save() 
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No hay registros'
            
        except Exception as e:
            data['error'] = str(e)
            
        return JsonResponse(data) 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición del servicio'
        context['entity'] = 'Servicios'
        context ['icon'] = 'fas fa-pencil-alt'
        context['list_url'] = reverse_lazy('servicios_list')
        context['action'] = 'edit'
        context['image_url'] = self.object.imagen.url if self.object.imagen else None

        return context

class ServicioDeleteView(LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    model = Servicios
    template_name = 'servicios/delete.html'
    success_url = reverse_lazy('servicios_list')
    permission_required = 'delete_servicios'
    url_redirect = success_url
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de Servicios'
        context['entity'] = 'Servicios'
        context['list_url'] = reverse_lazy('servicios_list')
        return context