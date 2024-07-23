from django.core.mail import send_mail
from django.conf import settings

def send_email_function(recipients, subject, message, sender=settings.EMAIL_HOST_USER):
    send_mail(
        subject,
        message,
        sender,
        recipients,
        fail_silently=False,
    )