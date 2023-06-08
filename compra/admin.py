from django.contrib import admin
from compra.models import Proveedor, Producto


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni')
    search_fields = ['nombre', 'apellido']


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'stock_actual', 'proveedor')
    search_fields = ['nombre', 'proveedor']

