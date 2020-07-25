from django.shortcuts import render

from autropolis_map.models import Game, Local, Super

def index(request):
    # Obtain data
    
    # Package data
    
    # Return data
    return render(request, 'index.html')


def page(request, pagername):
    # Obtain data
    
    # Package data
    
    # Return data
    return render(request, pagername + '.html')

from django.views import generic

class LocalListView(generic.ListView):
    model = Local
