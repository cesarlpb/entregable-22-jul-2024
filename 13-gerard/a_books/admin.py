from django.contrib import admin
from .models import Autor, Saga, Libro
# Register your models here.
 
admin.site.register(Autor)
admin.site.register(Saga)
admin.site.register(Libro)