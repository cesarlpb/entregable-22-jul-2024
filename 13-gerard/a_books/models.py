from django.db import models

# Create your models here. 
 
class Autor(models.Model):
    nombre = models.CharField(max_length=63)
    apellido = models.CharField(max_length=63)
 
    def __str__(self):
        return self.nombre
    

class Saga(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
 
    def __str__(self):
        return self.nombre


class Libro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=127)
    saga = models.ForeignKey(Saga, on_delete=models.CASCADE, null=True, blank=True)
    numero_saga = models.PositiveIntegerField(null=True, blank=True)
    caratula = models.ImageField(upload_to='media', default='static/images/image.png')
 
    def __str__(self):
        if self.saga:
            return f'{self.saga} ({self.numero_saga}) - {self.titulo}'
        else:
            return self.titulo