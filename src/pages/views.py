import os

from django import get_version
from django.conf import settings
from django.shortcuts import render

from products.ejemplo_clases import Producto, ProductoDigital

def home(request):
    # Producto físico
    producto1 = Producto("Camiseta", 25.00, 10)
    descuento_fisico = 20
    precio_original_fisico = producto1.precio
    producto1.aplicar_descuento(descuento_fisico)
    producto1.actualizar_stock(5)

    # Producto digital
    producto_digital1 = ProductoDigital("Curso de Python", 49.99, 1000, "PDF", 150)
    descuento_digital = 10
    precio_original_digital = producto_digital1.precio
    producto_digital1.aplicar_descuento(descuento_digital)

    context = {
        # Físico
        "producto_fisico": producto1.nombre,
        "producto_precio_original": f"{precio_original_fisico:.2f}",
        "producto_precio_descuento": f"{producto1.precio:.2f}",
        "producto_stock": producto1.stock,
        "producto_descuento": descuento_fisico,

        # Digital
        "producto_digital": producto_digital1.nombre,
        "producto_digital_precio_original": f"{precio_original_digital:.2f}",
        "producto_digital_precio_descuento": f"{producto_digital1.precio:.2f}",
        "producto_digital_descuento": descuento_digital,
        "mensaje_digital": producto_digital1.descargar(),
    }

    return render(request, "pages/home.html", context)


