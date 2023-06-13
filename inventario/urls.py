from django.contrib import admin
from django.urls import path
from inventario.views import listado,crearProducto

urlpatterns = [
    path('',listado),
    path('crear/',crearProducto,name='crear'),
    
]