from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView, UpdateView,DetailView
from system.models import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

class ServiciosListView(ListView):
    model = Servicios
    template_name = 'servicios/services.html'
    context_object_name = 'services'
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        catid = self.request.GET.get('categories')
        print(f"Filtrando por categoría ID: {catid}")
        if catid:
            queryset = Servicios.objects.filter(servicio_id=catid)
        print(queryset)# Ajusta el filtro según tu modelo y campo
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['services'] = Servicios.objects.all()
        context['tservices'] = TipoServicio.objects.all()
        context['active_filter'] = self.request.GET.get('categories', 'all')
        context['comp'] = Compania.objects.first()
        return context