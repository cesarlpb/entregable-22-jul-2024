from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('item/<int:id>/editar/', views.item_update, name='item_update'),
    path('item/<int:id>/borrar/', views.item_confirm_delete, name='item_confirm_delete'),
    path('item/crear/', views.item_create, name='item_create'),
]
