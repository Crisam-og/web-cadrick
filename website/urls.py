from django.urls import path, include
from website.views import *
from website.views.inicio.views import *
from website.views.nosotros.views import *
from website.views.cursos.views import *
from website.views.inscripciones.views import *
from website.views.error404.views import *
from website.views.servicios.views import *
from website.views.contactanos.views import *

from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('index/', IndexTemplateView.as_view(), name='index'),
    path('nosotros/', NosotrosListView.as_view(), name='nosotros'),
    path('servicios/list/', ServiciosListView.as_view(), name='servicios-list'),
    path('cursos/list/', CursoListView.as_view(), name='curso-list'),
    path('cursos/detalle-curso/<uuid:id>/', CursoDetailView.as_view(), name='detail-curso'),
    path('inscripciones/registro/', InscripcionesCreateView.as_view(), name='inscripciones-cursos'),
    path('contactanos/', ContactanosTemplateView.as_view(), name='contactanos'),
    path('error404/', Error404View.as_view(), name='error404'),
]