from django.forms import ModelForm
from .models import Proveedor, Producto


class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni']
        labels = {'numero_legajo': 'N° de Legajo'}


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']
        labels = {'stock_actual': 'Stock'}
