from django.db import models

# Create your models here.

"""
En esta parte crearemos nuestros MODELS (nuestras tablas)

PRODUCTO:
-id
-nombre
-precio
-stock

Para crear un Model, lo haremos del mismo modo que creamos UNA CLASE.
Cada MODEL, sera una Clase que heredara PROPIEDADES de la clase MODELS

"""

class Productos(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    precio = models.FloatField()
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    


