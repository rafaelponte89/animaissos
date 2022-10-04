from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from api_animais.models import Usuario
from .forms import CampaignRegisterForm, RegisterForm, UserUpdateForm
# Create your views here.

@login_required
def registerCampaign(request):

    if request.method == 'POST':
        form = CampaignRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Campanha cadastrada com sucesso!")
            return redirect('registerCampaign')
    else:
        form = CampaignRegisterForm()
    return render(request, 'cadastrar_campanha.html',{'form':form})


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

