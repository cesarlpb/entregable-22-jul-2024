from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from proyecto20.settings import EMAIL_HOST_RECEIVER
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = f'Mensaje de {name}'
            html_message = f"<h2>Mensaje:</h2><p>{message}</p>"
            # Ejemplo de foto:
            # <div>Foto random:<img src='https://plus.unsplash.com/premium_photo-1661856452176-d919ec23494a?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'></div>
            plain_message = message  # Puedes tener una versión en texto plano del mensaje
            send_mail(
                subject,
                plain_message,  # Este es el mensaje en texto plano
                email,
                [EMAIL_HOST_RECEIVER],  # Cambia esto por el email donde quieres recibir los mensajes
                fail_silently=False,
                html_message=html_message  # Este es el mensaje en HTML
            )
            return HttpResponseRedirect(reverse('contact:thanks'))
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def thanks_view(request):
    return render(request, 'contact/thanks.html')
