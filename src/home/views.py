from django.shortcuts import render
from property.models import Property, Category
from agents.models import Agent


def home(request):
    category_list_home = Category.objects.all()
    property_list_home = Property.objects.all()
    agent_list_home = Agent.objects.all()
    template = 'home.html'
    context = {
        'category_list_home': category_list_home,
        'property_list_home': property_list_home,
        'agent_list_home': agent_list_home,
    }
    return render(request, template, context)