from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from api_animais.models import Animal, Campanha, PortoSeguro, Usuario
from .forms import AnimalRegisterForm, CampaignRegisterForm, RegisterForm, UserUpdateForm, PortoSeguroForm
from django.views.generic import TemplateView
from datetime import date

# Create your views here.


@login_required
def registerAnimal(request):

    if request.POST:
        print(request.user)
        animal_form = AnimalRegisterForm(request.POST, request.FILES, initial={
                                         'username': request.user})
        if animal_form.is_valid():
            animal_form.save()
            messages.success(request, "Animal criado com sucesso!")
            return redirect('cadastrar_animais')
    else:
        animal_form = AnimalRegisterForm(initial={'username': request.user})

    return render(request, 'cadastrar_animal.html', {'form': animal_form})


@login_required
def updateAnimal(request, pk):
    # animal = get_object_or_404(Animal, pk=pk)
    animal = Animal.objects.filter(username=request.user).get(pk=pk)
    if request.POST:
        animal_form = AnimalRegisterForm(
            request.POST, request.FILES, instance=animal)
        if animal_form.is_valid():
            animal_form.save()
            messages.success(request, "Animal atualizado com sucesso!")
            return redirect('listar_animais')
    else:
        animal_form = AnimalRegisterForm(instance=animal)

    return render(request, 'cadastrar_animal.html', {'form': animal_form, 'animal': animal})


def getAnimais(request):

    animais = Animal.objects.filter(username=request.user.id)

    return render(request, 'listar_animais.html', {'animais': animais})


def encerrarCampanha(request, pk):
    campanha = Campanha.objects.filter(username=request.user).get(pk=pk)
    campanha.data_final = date.today()
    campanha.save()
    return redirect('listar_ativas')


def registerCampaign(request, pk):
    data = (date.today()).strftime('%d/%m/%Y')
    animal = Animal.objects.filter(username=request.user).get(pk=pk)

    if request.method == 'POST':

        # form_animal = AnimalRegisterForm(request.POST, request.FILES)
        form_campanha = CampaignRegisterForm(request.POST)
        print(form_campanha.is_valid())

        if form_campanha.is_valid():
            form_campanha.save()
            print(animal)
            # form_animal.save()
            messages.success(request, "Campanha cadastrada com sucesso!")
            return redirect('listar_ativas')
    else:
        form_campanha = CampaignRegisterForm(initial = {'username': request.user, 'animal':animal})
        # form_animal = AnimalRegisterForm(initial = {'username':request.user})
    
    contexto = {
        'form_campanha': form_campanha,
        'animal': animal,
        'data_inicial': data
    }
    return render(request, 'cadastrar_campanha.html',contexto)

def getCampanhas (request):

    campanhas = Campanha.objects.filter(username = request.user.id)
    
    return render(request,'listar_campanhas.html',{'campanhas':campanhas, 'status': 'Todas as suas'})

def getCampanhasAtivas(request):

    campanhas = Campanha.objects.filter(data_final = None).filter(username = request.user)

    return render(request,'listar_campanhas.html',{'campanhas':campanhas, 'status': 'Acontecendo'})


def getCampanhasEncerradas(request):
    campanhas = Campanha.objects.exclude(data_final = None ).filter( username = request.user)
    
    return render(request,'listar_campanhas.html',{'campanhas':campanhas, 'status': 'Encerradas'})



def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuário cadastrado com sucesso!")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})

def perfil(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'perfil.html',{ "usuario": usuario })

@login_required
def update(request):
    if request.POST:
        usuario = UserUpdateForm(request.POST, instance = request.user)
        if usuario.is_valid():
            usuario.save()
            messages.success(request,'Informações Atualizadas!')
            return redirect ('perfil', request.user.pk)
    else:
        usuario = UserUpdateForm(instance = request.user)
        
    context = {
        'usuario': usuario
    }

    return render(request, 'update.html',context)




def cadastrarPortoSeguro(request):

    form = None
    if request.user.is_authenticated:
        if request.method == "POST":  # se o método é Post
            form = PortoSeguroForm(request.POST)  # cria um objeto do tipo Contato (forms.py)
            if form.is_valid():  # se o formulário é válido, todos os campos requeridos estão de acordo
            
                form.save()  # salva informações
                messages.success(request,'Sucesso') # menssagem de sucesso
                return redirect('cadastrar_ponto')
            else:
                messages.error(request,'Algo saiu errado')
        else:
            form = PortoSeguroForm(initial={'username':request.user})
        
    pontos = PortoSeguro.objects.all()
    print(pontos)
    estrutura=''

    for p in pontos:
        estrutura = estrutura + '{'+"\"ponto\""+':\"'+ str(p.titulo) +'\",' \
                   +"\"lat\""+':\"'+ str(p.latitude)+'\",' \
                   +"\"long\""+':\"'+ str(p.longitude)+'\",' \
                   +"\"qtd_animais\""+':\"'+ str(p.qtd_animais)+ '\"},' \
                    
    estrutura = estrutura.strip(',')
   
    varios='{"pontos":[' + estrutura + ']}'

    print(varios)
    estrutura = estrutura[:len(estrutura)-1]

    
    return render(request, 'mapa.html',{ 'form': form, 'mapa': varios })


def carregarPortoSeguro(request):

    pontos = PortoSeguro.objects.all()
    print(pontos)
    estrutura=''

    for p in pontos:
        estrutura = estrutura + '{'+"\"ponto\""+':\"'+ str(p.titulo) +'\",' \
                   +"\"lat\""+':\"'+ str(p.latitude)+'\",' \
                   +"\"long\""+':\"'+ str(p.longitude)+'\",' \
                   +"\"qtd_animais\""+':\"'+ str(p.qtd_animais)+ '\"},' \
                    
    estrutura = estrutura.strip(',')
   
    varios='{"pontos":[' + estrutura + ']}'

    print(varios)
    estrutura = estrutura[:len(estrutura)-1]

    return render(request, 'exibir_mapa.html', {'mapa':varios})
