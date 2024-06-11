from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from system.models import *
from system.forms.nosotros.forms import *
from system.forms.servicios.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from system.mixin import *
from django.contrib.auth.mixins import LoginRequiredMixin

# PARTE NOSOTROS
class NosotrosListView(LoginRequiredMixin,ValidatePermissionRequiredMixin,ListView):
    model = Nosotros
    template_name = 'nosotros/list.html'
    permission_required = 'view_nosotros'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de nosotros'
        context['create_url'] = reverse_lazy('nosotros_create')
        return context

class NosotrosCreateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,CreateView):
    model = Nosotros
    form_class = NosotrosForm 
    template_name = 'nosotros/create.html' 
    success_url = reverse_lazy('nosotros_list')
    permission_required = 'add_nosotros'
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
        context['title'] = 'Registrar nosotros'
        context['entity'] = 'Nosotros'
        context ['icon'] = 'fas fa-plus'
        context['list_url'] = reverse_lazy('nosotros_list')
        context['action'] = 'add'
        return context
    
class NosotrosUpdateView(LoginRequiredMixin,ValidatePermissionRequiredMixin,UpdateView):
    model = Nosotros
    form_class = NosotrosForm
    template_name = 'nosotros/create.html'
    success_url = reverse_lazy('nosotros_list')
    permission_required = 'change_proyectos'
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
        context['title'] = 'Edición de nosotros'
        context['entity'] = 'Nosotros'
        context ['icon'] = 'fas fa-pencil-alt'
        context['list_url'] = reverse_lazy('nosotros_list')
        context['action'] = 'edit'

        return context
    
class NosotrosDeleteView(LoginRequiredMixin,ValidatePermissionRequiredMixin,DeleteView):
    model = Nosotros
    template_name = 'nosotros/delete.html'
    success_url = reverse_lazy('nostooros_list')
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
        context['title'] = 'Eliminación de Nosotros'
        context['entity'] = 'Nosotros'
        context['list_url'] = reverse_lazy('nosotros_list')
        return context