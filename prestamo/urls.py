from django.conf.urls import url 
from prestamo import views
from django.contrib.auth.decorators import login_required
# Create your views here.
urlpatterns = [

	url(r'^$', login_required(views.base), name='base'),
#CLIENTE URL
	url(r'^cliente/$', views.ClienteList.as_view(), name='cliente-list'),
	url(r'^cliente/(?P<pk>[0-9]+)/detail$', views.ClienteDetail.as_view(), name='cliente-detail'),    
    url(r'^cliente/(?P<pk>[0-9]+)/update/$', views.ClienteUpdate.as_view(), name='cliente-update'),
	url(r'^cliente/(?P<pk>[0-9]+)/delete/$', views.ClienteDelete.as_view(), name='cliente-delete'),
    url(r'^cliente/create/$', views.ClienteCreate.as_view(), name='cliente-create'),

#FORMULARIO URL

    url(r'^formulario/$', views.FormularioListView.as_view(), name='formulario-list'),
	url(r'^formulario/(?P<pk>[0-9]+)/detail/$', views.FormularioDetailView.as_view(), name='formulario-detail'),
	url(r'^formulario/(?P<pk>[0-9]+)/update/$', views.FormularioUpdate.as_view(), name='formulario-update'),
	url(r'^formulario/(?P<pk>[0-9]+)/delete/$', views.FormularioDelete.as_view(), name='formulario-delete'),
  	url(r'^formulario/create/$', views.FormularioCreate.as_view(), name='formulario-create'),

#RECURSOS URL

    url(r'^recursos/$', views.RecursoListView.as_view(), name='recursos-list'),
	url(r'^recursos/(?P<pk>[0-9]+)/detail/$', views.RecursoDetailView.as_view(), name='recursos-detail'),
	url(r'^recursos/(?P<pk>[0-9]+)/update/$', views.RecursoUpdate.as_view(), name='recursos-update'),
	url(r'^recursos/(?P<pk>[0-9]+)/delete/$', views.RecursoDelete.as_view(), name='recursos-delete'),
  	url(r'^recursos/create/$', views.RecursoCreate.as_view(), name='recursos-create'),

]