from django.db import models

# Create your models here.
class paises(models.Model):
    nombre_pais= models.CharField(max_length= 20)
    visita= models.IntegerField()
    idioma= models.CharField(max_length=20)
    
class hoteles(models.Model):
    nombre_hotel= models.CharField(max_length=20)
    ubicacion=models.CharField(max_length=20)
    


