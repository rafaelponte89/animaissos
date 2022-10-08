from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from api_animais.models import Animal, Campanha, Usuario
# from django.contrib.auth.models import User
from api_animais.models import Usuario
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,)
    last_name = forms.CharField(max_length = 50, required = True, )
    email = forms.EmailField(required = True)

    class Meta:
        model = Usuario
        fields = ['email','username','first_name','last_name','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(max_length = 50, required = True)
    last_name = forms.CharField(max_length = 50, required = True)

    class Meta:
        model = Usuario
        fields = ['email','first_name','last_name','username']

class CampaignRegisterForm(forms.ModelForm):
    #data_final = forms.DateField(required = True, widget = forms.NumberInput(attrs={'type':'date'}))
    titulo = forms.CharField(max_length = 150, required = True)
    finalidade = forms.CharField(max_length= 300, required = True, widget=forms.Textarea(attrs={'rows':3,'maxlength':250}))
    
    username = forms.ModelChoiceField(queryset = Usuario.objects.all(),
                widget = forms.HiddenInput())

    class Meta:
        model = Campanha
        fields = ['titulo','finalidade','username']

class AnimalRegisterForm(forms.ModelForm):
    apelido_animal = forms.CharField(
        max_length = 100, required= True
    )
    img_animal = forms.ImageField(required = True)
    username = forms.ModelChoiceField(queryset = Usuario.objects.all(),
                widget = forms.HiddenInput())
    class Meta:
        model = Animal
        fields = ['apelido_animal','img_animal','sit_animal','username']
        
    