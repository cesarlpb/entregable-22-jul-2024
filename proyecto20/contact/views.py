from django.shortcuts import render
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Mensaje de {name}',
                message,
                email,
                ['erikmuar91@gmail.com'],  # Cambia esto por el email donde quieres recibir los mensajes
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse('contact:thanks'))
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def thanks_view(request):
    return render(request, 'contact/thanks.html')
