# items/forms.py

from django import forms
from .models import Item
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio']
    
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.template_pack = 'bootstrap5'
        self.helper.add_input(Submit('submit', 'Save'))

        # Adding Bootstrap classes to form fields
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

