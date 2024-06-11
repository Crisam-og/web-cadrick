from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from system.models import *
from system.forms.proyectos.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from system.mixin import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ProyectoListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    model = Proyectos
    template_name = 'proyectos/list.html'
    permission_required = 'view_proyectos'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de proyectos'
        context['create_url'] = reverse_lazy('proyecto_create')
        return context

class ProyectoCreateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Proyectos
    form_class = ProyectoForm 
    template_name = 'proyectos/create.html' 
    success_url = reverse_lazy('proyecto_list')
    permission_required = 'add_proyectos'
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
        context['title'] = 'Registrar nuevo proyecto'
        context['entity'] = 'Proyectos'
        context ['icon'] = 'fas fa-plus'
        context['list_url'] = reverse_lazy('proyecto_list')
        context['action'] = 'add'

        return context
    
class ProyectoUpdateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Proyectos
    form_class = ProyectoForm
    template_name = 'proyectos/create.html'
    success_url = reverse_lazy('proyecto_list')
    permission_required = 'change_proyectos'
    url_redirect = success_url
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        # Establecer la fecha de inicio inicial
        initial['fecha_de_proyecto'] = self.object.fecha_de_proyecto.strftime('%Y-%m-%d')  # Formato YYYY-MM-DD
        return initial
    
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
        context['title'] = 'Edición de proyectos'
        context['entity'] = 'Proyectos'
        context ['icon'] = 'fas fa-pencil-alt'
        context['list_url'] = reverse_lazy('proyecto_list')
        context['action'] = 'edit'
        context['image_url'] = self.object.imagen.url if self.object.imagen else None

        return context

class ProyectoDeleteView(LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    model = Proyectos
    template_name = 'proyectos/delete.html'
    success_url = reverse_lazy('proyecto_list')
    permission_required = 'delete_proyectos'
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
        context['title'] = 'Eliminación de Proyectos'
        context['entity'] = 'Proyectos'
        context['list_url'] = reverse_lazy('proyecto_list')
        return context