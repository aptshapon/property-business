from django.shortcuts import render
from .models import ContactDetails


def send_mail(request):
    contactdetails = ContactDetails.objects.last()
    template = 'contact.html'
    context = {
        'contactdetails': contactdetails
    }

    return render(request, template, context)


def success(request):
    pass