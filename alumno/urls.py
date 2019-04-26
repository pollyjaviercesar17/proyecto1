from django.conf.urls import url
from django.contrib import admin
from alumno import views

from django.conf import settings

from django.conf.urls.static import static
urlpatterns = [
    url(r'^$', views.AlumnoListView.as_view(), name='list'),
    url(r'^listTrue/$', views.AlumnoTrueListView.as_view(), name='list_True'),
    url(r'^listFalse/$', views.AlumnoFalseListView.as_view(), name='list_False'),
    url(r'^listall/$', views.AlumnoallView.as_view(), name='list_all'),
    url(r'^(?P<pk>[-\ \w]+)/detail/$',
        views.AlumnoDetailView.as_view(), name='detail'),


    url(r'^(?P<pk>[-\ \w]+)/delete/$',
        views.AlumnoDeleteView.as_view(), name='delete'),
    url(r'^(?P<pk>[-\ \w]+)/update/$',
        views.AlumnoUpdateView.as_view(), name='update'),
    url(r'^add/$',
        views.AlumnoCreateView.as_view(), name='register'),
    
    #beca create
    url(r'^(?P<pk>[-\ \w]+)/add/beca$',
        views.AlumnoCreateViewBeca.as_view(), name='register_alumno'),
    #beca update
    url(r'^(?P<pk>[-\ \w]+)/update/beca$',
        views.AlumnoUpdateViewBeca.as_view(), name='update_alumno'),

    #urls vivienda
    url(r'^(?P<pk>[-\ \w]+)/vivienda/add/$',
        views.ViviendaCreateView.as_view(), name='register_vivienda'),

    url(r'^(?P<pk>[-\ \w]+)/vivienda/actualizar/$',
        views.ViviendaUpdateView.as_view(), name='update_vivienda'),

    url(r'^(?P<pk>[-\ \w]+)/datosfamiliar/detail/$',
        views.DatosFamiliarDetailView.as_view(), name='detail_datosfamiliar'),


    url(r'^(?P<pk>[-\ \w]+)/datosfamiliar/add/$',
        views.DatosFamiliarCreateView.as_view(), name='register_datosfamiliar'),


    url(r'^(?P<pk>[-\ \w]+)/datosfamiliar/delete/$',
        views.DatosFamiliarDeleteView.as_view(), name='delete_datosfamiliar'),


    url(r'^(?P<pk>[-\ \w]+)/fame/add/$',
        views.DatosFameCreateView.as_view(), name='register_fame'),
    


    url(r'^(?P<pk>[-\ \w]+)/fame/actualizar/$',
        views.DatosFameUpdateView.as_view(), name='update_fame'),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


