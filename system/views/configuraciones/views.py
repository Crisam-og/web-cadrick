from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView
from system.models import *
from system.forms.configuraciones.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from system.mixin import *
from django.contrib.auth.mixins import LoginRequiredMixin

class ConfigListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    model = Configuraciones
    template_name = 'config/list.html'
    permission_required = 'view_configuraciones'
   
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Listado de Configuraciones del Sitio Web'
        #context['create_url'] = reverse_lazy('config_create')
        return context
    
# class ConfigCreateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
#     model = Cursos
#     form_class = CursosForm
#     template_name = 'cursos/create.html'
#     success_url = reverse_lazy('cursos_list')
#     permission_required = 'system.add_configuraciones'

#     url_redirect = success_url
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
        
#     def post(self, request, *args, **kwargs):
#         data = {}
        
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
                
#                 if form.is_valid():
#                     form.save()
                    
#                 else:
#                     data['error'] = form.errors
#             else: 
#                 data['error'] = 'Ha ocurrido un error'
#         except Exception as e:
#             data['error'] = str(e)
            
#         return JsonResponse(data)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context ['title'] = 'Registrar nuevo Curso'
#         context ['entity'] = 'Cursos'
#         context ['icon'] = 'fas fa-plus'
#         context ['list_url'] = reverse_lazy('cursos_list')
#         context['action'] = 'add'
#         return context
    
class ConfigUpdateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Configuraciones
    form_class = ConfigForm
    template_name = 'config/create.html'
    success_url = reverse_lazy('config_update')
    permission_required = 'change_configuraciones'
    url_redirect = success_url
    
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_initial(self):
        initial = super().get_initial()
        # Establecer la fecha de inicio inicial
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
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
            
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar valor de configuraciones'
        context ['entity'] = 'Configuraciones'
        context ['icon'] = 'fas fa-pencil-alt'
        context['list_url'] = reverse_lazy('config_list')
        context['action'] = 'edit'
        return context
    
# class ConfigDeleteView(DeleteView):
#     model = Cursos
#     template_name = 'cursos/delete.html'
#     success_url = reverse_lazy('cursos_list')
    
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)
#     def post(self, request, *args, **kwargs):
#         data = {}
        
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
            
#         return JsonResponse(data)
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context ['title'] = 'Eliminar curso'
#         context ['entity'] = 'Cursos'
#         context['list_url'] = reverse_lazy('cursos_list')
#         return context