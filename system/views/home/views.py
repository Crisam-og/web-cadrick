from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView
from system.models import *
from system.forms import *
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from time import gmtime, strftime
from django.dispatch import receiver
# Importar el modelo User
from user.models import User
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.mixins import LoginRequiredMixin
# @receiver(user_logged_in)
# def get_group_on_login(sender, user, request, **kwargs):
#     user.get_group_session()

class HomeTemplateView(LoginRequiredMixin,TemplateView):
    template_name = 'home/index.html'

    #@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # def get(self, request, *args, **kwargs):
        
    #     group = request.user.get_group_session()
    #     print(group)
    #     if group:
    #         request.session['group_id'] = group.pk
    #     else:
    #         request.session['group_id'] = None  # Establecer None si no hay grupo
    #     return super().get(request, *args, **kwargs)
    
    # def get(self, request, *args, **kwargs):
    #     print(request.user.get_group_session())  
    #     request.user.get_group_session()  
    #     return super().get(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        # print(f"Resp: {request} ")
        # print(f"Resp: {request.user.get_group_session()} ")
        # request.user.get_group_session()
        user = request.user
        print(f"Usuario obtenido: {user}")
        group = user.get_group_session()
        print(f"Grupos obtenidos: {group}")
        #group_name = group.name if group else None
        return super().get(request,*args, **kwargs)

        #return super().get(request, group_name=group_name,*args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos'] = Proyectos.objects.all().count()
        context['equipo'] = Equipo.objects.all().count()
        context['cursos'] = Cursos.objects.all().count()
        context['servicios'] = Servicios.objects.all().count()
        context['clientes'] = Clientes.objects.all().count()
        context['capacitadores'] = Clientes.objects.all().count()
        context['inscripciones'] = Inscripciones.objects.all().count()
        context['formatted_datetime'] = format(datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
        #context['formatted_datetime'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        #context['current_group'] = self.request.user.get_current_group(self.request)
        #context['current_group'] = self.request.session.get('current_group')
        return context