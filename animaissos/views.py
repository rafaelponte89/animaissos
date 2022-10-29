from django.shortcuts import render
from api_animais.models import Campanha, Animal


def index(request):
    pesquisa = request.GET.get('pesquisa','')
    # Seleciona todas as campanhas ativas
    campanhas = Campanha.objects.filter(data_final = None)

    if pesquisa:
        campanhas = campanhas.filter(titulo__icontains=pesquisa) | campanhas.filter(informacoes__icontains=pesquisa)



    return render(request, 'listar_campanhas.html', {'campanhas':campanhas})

