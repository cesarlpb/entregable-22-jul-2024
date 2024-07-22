

from django.urls import path
from .views import contact_view, thanks_view

app_name = 'contact'

urlpatterns = [
    path('', contact_view, name='contact'),
    path('thanks/', thanks_view, name='thanks'),
]
