from django.db import models


class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

    def nombrecompleto(self):
        return f'{self.nombre} {self.apellido}'

    def __str__(self):
        return self.nombrecompleto()


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'
