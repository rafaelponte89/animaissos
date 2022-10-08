from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from api_animais.models import Animal, Campanha, Usuario
from .forms import AnimalRegisterForm, CampaignRegisterForm, RegisterForm, UserUpdateForm
# Create your views here.

from django.views.generic import TemplateView

from datetime import date

@login_required
def registerAnimal(request):

    if request.POST:
        print(request.user)
        animal_form = AnimalRegisterForm( request.POST, request.FILES, initial={'username':request.user}  )
        if  animal_form.is_valid():
            animal_form.save()
            messages.success(request, "Animal criado com sucesso!")
            return redirect('cadastrar_animais')
    else:
        animal_form = AnimalRegisterForm( initial={'username':request.user}  )

    return render(request, 'cadastrar_animal.html', {'form':animal_form})

def getAnimais(request):

    animais = Animal.objects.filter(username = request.user.id)

    return render(request, 'listar_animais.html',{'animais':animais})



def registerCampaign(request):
    data = (date.today()).strftime('%d/%m/%Y')
    if request.method == 'POST':
        # form_animal = AnimalRegisterForm(request.POST, request.FILES)
        form_campanha = CampaignRegisterForm(request.POST)
        if form_campanha.is_valid():
            form_campanha.save()
            # form_animal.save()
            messages.success(request, "Campanha cadastrada com sucesso!")
            return redirect('iniciar_campanha')
    else:
        form_campanha = CampaignRegisterForm(initial = {'username': request.user})
        # form_animal = AnimalRegisterForm(initial = {'username':request.user})
    
    contexto = {
        'form_campanha': form_campanha,
        # 'form_animal': form_animal,
        'data_inicial': data
    }
    return render(request, 'cadastrar_campanha.html',contexto)

def getCampanhas (request):

    campanhas = Campanha.objects.filter(username = request.user.id)
    
    return render(request,'listar_campanhas.html',{'campanhas':campanhas})

def getCampanhasAtivas(request):
    campanhas = Campanha.objects.filter(data_final = None).filter(username = request.user)
                        
    return render(request,'listar_campanhas.html',{'campanhas':campanhas})


def getCampanhasEncerradas(request):
    campanhas = Campanha.objects.exclude(data_final = None ).filter( username = request.user)

    return render(request,'listar_campanhas.html',{'campanhas':campanhas})



def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuário cadastrado com sucesso!")
            return redirect('register')
    else:
        form = RegisterForm()
    return render(request, 'register.html',{'form':form})

def perfil(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'perfil.html',{"usuario":usuario})

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


