from datetime import date
from distutils.log import info
from operator import is_
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from web.forms import formpaises
from .models import paises, hoteles
from django.template import loader
from  .forms import formpaises
# Create your views here.

def inicio(request):
    return render (request, "index.html")


def listado(request):
    objeto= paises (nombre_pais= "Italia", visita= 2015, idioma="Italiano" )
    objeto.save()
 
    return HttpResponse("EAT AND TRAVEL")


def sobremi (request):
    return render (request, "sofia.html")

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

def busqueda (request):
    return render (request, "busqueda.html")


    
def buscar(request):
    var2 = paises.objects.all()
    contexto2= { "todos" : var2 }
    
    if request.GET:
        var2 = request.GET["buscar"]

    buscador = paises.objects.filter(nombre_pais__icontains = var2)

    contexto2 = { "web" : buscador , "todos" : var2 }

    plantilla = loader.get_template("buscados.html")
    documento2 = plantilla.render( contexto2 )

    return HttpResponse( documento2 )

   

    # return HttpResponse( documento )
    # if request.GET ["nombre"]:
    #     nombre= request.GET ["nombre"]
    #     paises= paises.objects.filter(nombre_icointeins=nombre)
    #     return render (request, )
    # return HttpResponse (respuesta)    
        


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


