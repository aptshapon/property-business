from django.shortcuts import render
from property.models import Property, Category


def home(request):
    category_list = Category.objects.all()
    property_list = Property.objects.all()
    template = 'home.html'
    context = {
        'category_list': category_list,
        'property_list': property_list,
    }
    return render(request, template, context)