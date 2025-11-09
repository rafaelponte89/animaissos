from django.shortcuts import render
from api_animais.models import Campanha, Animal
from django.shortcuts import redirect
from django.contrib.auth import logout


def index(request):
    pesquisa = request.GET.get('pesquisa','')
    # Seleciona todas as campanhas ativas
    campanhas = Campanha.objects.filter(data_final = None)

    if pesquisa:
        campanhas = campanhas.filter(titulo__icontains=pesquisa) | campanhas.filter(informacoes__icontains=pesquisa)



    return render(request, 'listar_campanhas.html', {'campanhas':campanhas})


def logout_view(request):
    logout(request)
    return redirect('index')