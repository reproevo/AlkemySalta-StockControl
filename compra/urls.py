from django.urls import path

from compra import views

urlpatterns = [
    path('', views.home, name='home'),
    path('proveedores/nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedores/eliminar/<int:proveedor_id>', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('proveedores/listado', views.listado_proveedores, name="proveedores"),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/eliminar/<int:producto_id>', views.eliminar_producto, name='eliminar_producto'),
    path('productos/listado', views.listado_productos, name="productos"),
]
