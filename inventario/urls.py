from django.contrib import admin
from django.urls import path
from inventario.views import listado,crearProducto,editarProducto,eliminarProducto

#configs para estilos de CSS
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',listado,name='base'),
    path('crear/',crearProducto,name='crear'),
    path('editar/<id>',editarProducto,name='editar'),
    path('eliminar/<id>',eliminarProducto,name='eliminar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #agregar a la carga de las paginas