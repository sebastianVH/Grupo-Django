from django.contrib import admin
from django.urls import path
from inventario.views import despedida,saludar

urlpatterns = [
    path('saludar/',saludar),
    path('despedida/',despedida),
]