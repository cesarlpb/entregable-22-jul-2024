from django.forms import ModelForm
from django import forms
from .models import Autor, Saga, Libro

class FiltrarLibrosForm(forms.Form):
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=False)
    saga = forms.ChoiceField(choices=[])
    libro = forms.ModelChoiceField(queryset=Libro.objects.all(), required=False)