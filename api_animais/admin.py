from django.contrib import admin

from .models import Animal, Campanha, PortoSeguro, Usuario

from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register([Animal,Campanha,PortoSeguro,Usuario])

# admin.site.register(Usuario, UserAdmin)