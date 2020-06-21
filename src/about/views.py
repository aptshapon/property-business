from django.shortcuts import render
from .models import About


def aboutus(request):
    about = About.objects.last()
    template = 'about.html'
    context = {
        'about': about
    }
    return render(request, template, context)