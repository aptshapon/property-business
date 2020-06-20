from django.shortcuts import render
from .models import Property, Category


def property_list(request):
    property_list = Property.objects.all()
    template = 'property/list.html'
    context = {
        'property_list': property_list
    }

    return render(request, template, context)


def property_detail(request, id):
    property_detail = Property.objects.get(id=id)
    template = 'property/detail.html'
    context = {
        'property_detail': property_detail
    }

    return render(request, template, context)