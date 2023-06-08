from django.shortcuts import render, redirect
from .models import Proveedor, Producto
from .forms import ProveedorForm, ProductoForm


def listado_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'proveedores.html', {'proveedores': proveedores})


def nuevo_proveedor(request):
    form = ProveedorForm()
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('proveedores')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Enviar", "url_value": 'proveedores'})


def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def nuevo_producto(request):
    form = ProductoForm()
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
    return render(request, 'form_generico.html', {"form": form, "submit_value": "Enviar", "url_value": 'productos'})


def home(request):
    return render(request, 'homepage.html')


def eliminar_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.filter(id=proveedor_id).first()
    proveedor.delete()
    return redirect('proveedores')


def eliminar_producto(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    producto.delete()
    return redirect('productos')
