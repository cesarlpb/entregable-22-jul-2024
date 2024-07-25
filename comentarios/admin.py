from django.contrib import admin

from comentarios.models import Articulo, Comentario

admin.site.register(Articulo)
admin.site.register(Comentario)