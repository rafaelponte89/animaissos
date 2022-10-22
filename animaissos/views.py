from django.shortcuts import render
from api_animais.models import Campanha, Animal


def index(request):

    # Seleciona todas as campanhas ativas
    campanhas = Campanha.objects.filter(data_final = None)
    
    return render(request, 'listar_campanhas.html', {'campanhas':campanhas})

