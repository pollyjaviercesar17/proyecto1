from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
#importacion de vista
from reporte import views


urlpatterns = [
    url(r'^listado/alumno$', views.ListarAlumno.as_view(), name='list_all'),
    url(r'^listado/alumno/suspendido$', views.ListarAlumnoFalse.as_view(), name='list_false'),
    url(r'^listado/alumno/aprobado$', views.ListarAlumnoTrue.as_view(), name='list_true'),
    url(r'^alumno/(?P<pk>[-\ \w]+)$', views.PlanillaBeca.as_view(), name='planilla'),
    
    ]
