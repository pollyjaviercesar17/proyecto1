from django.conf.urls import url

from acta import views


urlpatterns = [


    url(r'^(?P<pk>[-\ \w]+)/update/$',
        views.ActaUpdateView.as_view(), name='renovar'),

    url(r'^(?P<pk>[-\ \w]+)/add/$',views.ActaCreateView.as_view(), name='register'),



    ]