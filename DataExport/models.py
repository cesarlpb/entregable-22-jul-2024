from django.db import models

class Facturacion(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)