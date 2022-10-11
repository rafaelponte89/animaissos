from cProfile import label
from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from api_animais.models import Animal, Campanha, PortoSeguro, Usuario
# from django.contrib.auth.models import User
from api_animais.models import Usuario


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True,)
    last_name = forms.CharField(max_length=50, required=True, )
    email = forms.EmailField(required=True)

    class Meta:
        model = Usuario
        fields = ['email', 'username', 'first_name',
            'last_name', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Usuario
        fields = ['email', 'first_name', 'last_name', 'username']


class CampaignRegisterForm(forms.ModelForm):
    # data_final = forms.DateField(required = True, widget = forms.NumberInput(attrs={'type':'date'}))
    titulo = forms.CharField(max_length=100, required=True)
    finalidade = forms.CharField(max_length=300, required=True, widget=forms.Textarea(
        attrs={'rows': 3, 'maxlength': 250}))

    username = forms.ModelChoiceField(queryset=Usuario.objects.all(),
                widget=forms.HiddenInput())

    animal = forms.ModelChoiceField(queryset=Animal.objects.all())

    class Meta:
        model = Campanha
        fields = ['titulo', 'finalidade', 'animal', 'username']


class AnimalRegisterForm(forms.ModelForm):
    apelido_animal = forms.CharField(
        max_length=100, required=True
    )
    img_animal = forms.ImageField(required=True)
    username = forms.ModelChoiceField(queryset=Usuario.objects.all(),
                widget=forms.HiddenInput())

    class Meta:
        model = Animal
        fields = ['apelido_animal', 'img_animal', 'sit_animal', 'username']


class PortoSeguroForm(forms.ModelForm):
    
    DISPONIVEL = (
            ('S', 'SIM'),
            ('N', 'NÃO')
        )

    latitude = forms.FloatField(required=True);
    longitude = forms.FloatField(required=True)
    titulo = forms.CharField(max_length=100, required=True)
    casa = forms.SelectMultiple( choices=DISPONIVEL)
    protetor = forms.SelectMultiple(choices=DISPONIVEL)
    qtd_animais = forms.IntegerField(required = True, min_value= 0, max_value = 30, help_text='Quantidade de animais de 0 a 30')
    username = forms.ModelChoiceField(queryset = Usuario.objects.all(),
                widget = forms.HiddenInput())
    

    # atribui propriedades à página html em sua geração, no caso aquelas propriedades recebem as respectivas classes css
    latitude.widget.attrs.update({'id': 'latitude','readonly':'true'})
    longitude.widget.attrs.update({'id': 'longitude','readonly':'true'})
#     titulo.widget.attrs.update({'class': 'validate'})
    
  
 
    class Meta:
        model = PortoSeguro
        fields = ['latitude', 'longitude', 'titulo','casa','protetor','username','qtd_animais']

 
   
    