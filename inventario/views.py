from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

"""
Aqui vamos a tener el RENDERIZADO de nuestros models

Vamos a tener las FUNCIONES que nos permiten definir QUE VAMOS A RENDERIZAR, DONDE , Y COMO
"""

def saludar(request):
    return render(request,'base.html')

def despedida(request):
    return HttpResponse(" Adios! Salida de la pagina")

def listado(request):
    return render(request,'listado.html')
