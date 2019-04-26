from django.conf.urls import url
from django.contrib import admin
from login import  views



urlpatterns = [
	url(r'^$', views.HomeTemplateView.as_view(), name='home'),
	url(r'^login/$', views.LoginView.as_view(), name='panel-login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='panel-logout'),
	url(r'^change/$', 
        views.Change_password, name='change_password'),

	
	]



