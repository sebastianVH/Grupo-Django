#aqui crearemos nuestros formularios,los cuales me van a permitir hacer la carga, mucho mas eficiente y rapida
#* Ventaja: evitamos tener que agregar campo por campo, cada detalle que estemos precisando
#* desventaja: no presentan ningun tipo de estilo, por lo cual, debemos nosotros, a traves de CSS, darle un diseño

#desde Django, debemos traernos el metodo, junto la clase de Formularios

from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):   
        class Meta:
            model = Productos
            fields = ['nombre','precio','stock','categoria']
    