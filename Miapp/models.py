from django.db import models

class Item(models.Model):
    nombre = models.CharField(max_length=100,null=True, blank=False)
    descripcion = models.TextField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)

    def __str__(self):
        return self.nombre, self.descripcion, self.precio