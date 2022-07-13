from django.urls import path
from web import views
from web.models import paises

urlpatterns = [
    path ("inicio/", views.inicio, name="inicio"), 
    path("listado/", views.listado),
    path("vista/", views.vistapaises, name="vista_p"),
    path ("hoteles/", views.vistahoteles),
    path ("info/", views.sobremi, name= "sofiab"),
    path("busqueda/", views.busqueda, name="buscar"),
    path ("buscarr/", views.buscar,name="buscarr"),
   
]