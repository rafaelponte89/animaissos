from django.contrib import admin

from .models import Animal, Campanha, PortoSeguro
# Register your models here.

admin.site.register([Animal,Campanha,PortoSeguro])
