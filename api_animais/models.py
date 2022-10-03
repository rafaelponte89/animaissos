from datetime import date
from distutils.command.upload import upload
from time import strftime
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):

    username = models.CharField(max_length=50, unique=True, error_messages={'unique': 'O usuário cadastrado já existe!'})
    password = models.CharField(max_length = 8)
    email = models.EmailField(max_length=254, unique = True, error_messages = {'unique':'O email cadastrado já existe!'})
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default= False)

    # USERNAME_FIELD = 'email'



class Animal(models.Model):

    SITUACAO_ANIMAL = \
    (
        ('R','RUA'),
        ('T','TRATAMENTO'),
        ('A','ADOTADO'),
        ('L','LAR TEMPORÁRIO')
    )
    apelido_animal = models.CharField(max_length=100,null=False,blank=False)
    img_animal = models.ImageField(upload_to='fotos_animais')
    sit_animal = models.CharField(max_length=50, choices=SITUACAO_ANIMAL)
    #username = models.ForeignKey(Usuario, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return f'{self.apelido_animal}' 

class Campanha(models.Model):
    data_inicial = models.DateField(default=(date.today()), editable=False)
    data_final = models.DateField()
    titulo = models.CharField(max_length=100, null=False, blank=False)
    finalidade = models.TextField(max_length=250, null=False,blank=False)
    username = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.titulo}'

class PortoSeguro(models.Model):
    DISPONIVEL = \
        (
            ('S','SIM'),
            ('N','NÃO')
        )
    latitude = models.FloatField()
    longitude= models.FloatField()
    titulo = models.CharField(max_length=200, unique=True)
    casa = models.CharField(max_length=1, choices = DISPONIVEL, verbose_name='Disponível: Casa, Água, Comida')
    protetor = models.CharField(max_length=1, choices=DISPONIVEL)
    qtd_animais = models.IntegerField(null=False, blank=False) 
    username = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.latitude}{self.longitude}'