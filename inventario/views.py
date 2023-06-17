from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productos

# Create your views here.

"""
Aqui vamos a tener el RENDERIZADO de nuestros models

Vamos a tener las FUNCIONES que nos permiten definir QUE VAMOS A RENDERIZAR, DONDE , Y COMO
"""

def listado(request):
    productos = Productos.objects.all() #estoy trajendo TODOS mis productos
    #creamos el "contexto" => es la manera de decirle a Django como va a representar a mis productos en mi HTML
    context = {"productos":productos}
    return render(request,'listado.html',context)

def crearProducto(request):
    # capturar el dato y guardarlo
    nombre = request.POST["nombre"] #indicamos el IDENTIFICADOR del campo en el cual nosotros recibimos los datos
    precio = request.POST["precio"]
    stock = request.POST["stock"]
    producto = Productos(nombre=nombre,precio=precio,stock=stock)
    producto.save() #NECESITO SI O SI EL SAVE PARA GUARDAR EL PRODUCTO EN MI BASE DE DATOS
    return redirect('/')

def eliminarProducto(request,id):
    producto = Productos.objects.get(id=id)
    producto.delete()
    return redirect('/')

def editarProducto(request,id):
    #busco el producto que voy a actualizar
    producto = Productos.objects.get(id=id)
    
    if request.method == 'GET':
        #debo elegir y enviar el producto
        ctx = {'producto':producto}
        return render(request,'editar.html',ctx)
        
    elif request.method == 'POST':
        #capturo los datos de mi POST
        nuevo_nombre = request.POST["nombre"]
        nuevo_precio = request.POST["precio"]
        nuevo_stock = request.POST["stock"]
        #asigno esos datos del post a mi producto
        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock
        producto.save() #NECESITO SI O SI EL SAVE PARA GUARDAR EL PRODUCTO EN MI BASE DE DATOS
        return redirect('/')
    
    return HttpResponse(f"Editar el id {id}")