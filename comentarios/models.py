from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, related_name='comentarios', on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto[:20]
