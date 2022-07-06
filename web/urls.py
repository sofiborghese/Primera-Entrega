from django.urls import path
from web import views

urlpatterns = [
    path ("inicio/", views.inicio), 
    path("listado/", views.listado),
    path("vista/", views.vistapaises),
    path ("hoteles/", views.vistahoteles),
   
]