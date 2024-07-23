from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/like/', views.add_like, name='add_like'),
    path('post/<int:post_id>/unlike/', views.remove_like, name='remove_like'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('post/', views.post_list, name='post_list'), TODO: hacer lista de posts :)
]

    

