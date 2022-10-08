from django.shortcuts import render
from api_animais.models import Campanha, Animal


def index(request):
    campanhas = Campanha.objects.filter(data_final = None)
    
    return render(request, 'index.html', {'campanhas':campanhas})

