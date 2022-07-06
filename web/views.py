from datetime import date
from distutils.log import info
from django.shortcuts import render
from django.http import HttpResponse
from .models import paises, hoteles
from django.template import loader
# Create your views here.

def inicio(request):
    return HttpResponse ("Bienvenidos a mi primer Blog")

def listado(request):
    objeto= paises (nombre_pais= "Italia", visita= 2015, idioma="Italiano" )
    objeto.save()
 
    return HttpResponse("EAT AND TRAVEL")


def vistapaises (request):
    if request.GET:
        nombrepais = str( request.GET['nombre_pais'] )
        
        visitar = int( request.GET['visita'] )
        
        idiomas = str( request.GET['idioma'] )
        
        
        objeto2 = paises( nombre_pais= nombrepais , visita= visitar , idioma= idiomas)
        objeto2.save()
    
    info= paises.objects.all()
    contexto= {"web" : info }
    plantilla=loader.get_template("html1.html")
    documento= plantilla.render(contexto)

    
    return HttpResponse( documento )

def vistahoteles (request):
    if request.GET:
        nombrehotel = str( request.GET['nombre_hotel'] )
        ubicaciones = str(request.GET['ubicacion'] )
        
        objeto3 = hoteles( nombre_hotel= nombrehotel , ubicacion= ubicaciones)
        objeto3.save()
    
    info1= hoteles.objects.all()
    contexto1= {"web": info1 }
    plantilla1=loader.get_template("html2.html")
    documento1= plantilla1.render(contexto1)

    
    return HttpResponse( documento1)


