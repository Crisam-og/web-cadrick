from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from system.models import *
from system.forms.publicidad.forms import *
from system.forms.servicios.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from system.mixin import *
from django.contrib.auth.mixins import LoginRequiredMixin


# class GaleriaListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
#     model = Galeria
#     template_name = 'publicidad/list.html'
#     permission_required = 'view_publicidad'
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Listado de publicidad'
#         context['create_url'] = reverse_lazy('publicidad_create')
#         return context

class GaleriaCreateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Galeria
    form_class = GaleriaForm 
    template_name = 'publicidad/create.html' 
    success_url = reverse_lazy('galeria_update')
    permission_required = 'add_publicidad'
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
        context['title'] = 'Edición de Textos y Imagenes'
        context['entity'] = 'Galeria'
        context ['icon'] = 'fas fa-plus'
        context['list_url'] = reverse_lazy('galeria_update')
        context['action'] = 'add'
        return context
    
class GaleriaUpdateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Galeria
    form_class = GaleriaForm 
    template_name = 'publicidad/create.html'
    success_url = reverse_lazy('publicidad_list')
    permission_required = 'change_publicidad'
    url_redirect = success_url
    def dispatch(self, request, *args, **kwargs):
        # Verifica si hay alguna instancia de Compania
        if not Galeria.objects.exists():
            return redirect('galeria_create')
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        try:
            # Obtener la única instancia de Compania
            return Galeria.objects.get()
        except Galeria.MultipleObjectsReturned:
            # Si hay múltiples, obtener la primera y eliminar las demás
            galerias = Galeria.objects.all()
            instance = galerias.first()
            # Eliminar las demás instancias
            galerias.exclude(pk=instance.pk).delete()
            return instance
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST.get('action', '')
            if action == 'edit':
                instance = self.get_object()
                form = self.get_form_class()(request.POST, instance=instance)
                if form.is_valid():
                    form.save()
                    data['success'] = True
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de Textos y Imagenes'
        context['entity'] = 'Galeria'
        context ['icon'] = 'fas fa-pencil-alt'
        context['list_url'] = reverse_lazy('galeria_update')
        context['action'] = 'edit'

        return context
    
# class GaleriaDeleteView(LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
#     model = Galeria
#     template_name = 'publicidad/delete.html'
#     success_url = reverse_lazy('publicidad_list')
#     permission_required = 'delete_publicidad'
#     url_redirect = success_url
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
#         context['title'] = 'Eliminación de Imagenes'
#         context['entity'] = 'Publicidad'
#         context['list_url'] = reverse_lazy('publicidad_list')
#         return context