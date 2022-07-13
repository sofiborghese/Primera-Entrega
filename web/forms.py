from django import forms

class formpaises (forms.Form):
    Nombre_del_pais_visitado= forms.CharField(max_length= 20)
    Año_de_visita= forms.IntegerField()
    Idioma= forms.CharField(max_length=20)
    
class BusquedaPaises (forms.Form):
    nombre = forms.CharField (max_length=20)