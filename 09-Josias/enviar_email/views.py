from django.shortcuts import render
from .emails import send_email_function

def send_email(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        recipients = [subject]

        send_email_function(recipients, subject, message)
        
        return render(request, 'email_sent.html')
    return render(request, 'send_email.html')
