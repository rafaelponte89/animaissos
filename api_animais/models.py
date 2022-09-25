from datetime import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):

    SITUACAO_ANIMAL = \
    (
        ('R','RUA'),
        ('T','TRATAMENTO'),
        ('A','ADOTADO'),
        ('L','LAR TEMPORÁRIO')
    )
    apelido_animal = models.CharField(max_length=100,null=False,blank=False)
    img_animal = models.ImageField()
    sit_animal = models.CharField(max_length=50, choices=SITUACAO_ANIMAL)

    def __str__(self):
        return f'{self.apelido_animal}' 

class Campanha(models.Model):
    data_inicial = models.DateField(auto_now=datetime.date)
    data_final = models.DateField()
    titulo = models.CharField(max_length=100, null=False, blank=False)
    finalidade = models.CharField(max_length=250, null=False,blank=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

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
    titulo = models.TextField(default=f'{User.email} | \
    {latitude} | {longitude}')
    casa = models.CharField(max_length=1, choices = DISPONIVEL, verbose_name='Disponível: Casa, Água, Comida')
    protetor = models.CharField(max_length=1, choices=DISPONIVEL)
    qtd_animais = models.IntegerField(null=False, blank=False) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.latitude}{self.longitude}'