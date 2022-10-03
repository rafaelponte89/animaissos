from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


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

def login(request):
    return render (request,'cadastrar_animal.html',{})