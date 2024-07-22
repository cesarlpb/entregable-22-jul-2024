from django import forms
from .models import Facturacion

class FacturacionForm(forms.ModelForm):
    class Meta:
        model = Facturacion
        fields = ['nombre_cliente', 'direccion', 'producto', 'cantidad', 'precio_total']