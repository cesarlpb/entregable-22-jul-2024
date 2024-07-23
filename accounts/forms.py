from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Introduce un email válido.')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self): 
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Usuario ya registrado")
        return username
        

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email ya registrado")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email'].lower()  # Guardar en minúsculas
        if commit:
            user.save()
        return user
    

    