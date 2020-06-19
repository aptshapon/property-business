from django.shortcuts import render
from .models import Property, Category


def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'
    context = {
        'property_list': property_list
    }

    return render(request, template, context)


def property_detail(request):
    pass