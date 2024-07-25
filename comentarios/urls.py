from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_articulos, name='lista_articulos'),
    path('articulo/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
]
