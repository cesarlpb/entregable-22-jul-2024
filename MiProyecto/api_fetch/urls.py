from django.contrib import admin
from django.urls import path, include
from .views import fetch_data_view

urlpatterns = [
    # path('', get_posts, name='get_posts'),
    path('data/', fetch_data_view, name='fetch-data-view'),
]
