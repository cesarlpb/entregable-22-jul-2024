from django.urls import path
from .views import busqueda_libros, libros, sagas

urlpatterns = [
    path('libros/', busqueda_libros, name='busqueda_libros'),
    path('sagas/<int:autor_id>/', sagas, name='cargar_sagas'),
    path('cargar-libros/', libros, name='cargar_libros'),
]