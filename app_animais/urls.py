from django.urls.conf import path
from .views import cadastrarPortoSeguro, register, perfil, registerAnimal, \
                registerCampaign, update, getAnimais, \
                getCampanhas, getCampanhasAtivas, getCampanhasEncerradas, updateAnimal \
                    

from django.contrib.auth import views as auth_views


urlpatterns = [

    # Usuário
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/<int:pk>', perfil, name='perfil'),
    path('perfil/update/', update, name='update'),
    path('register/', register, name='register'),

    # Animal
    path('animal/cadastrar/', registerAnimal, name='cadastrar_animais'),
    path('animal/listar/', getAnimais, name='listar_animais'),
    path('animal/listar/<int:pk>', updateAnimal, name = 'atualizar_animais'),

    # Campanha
    path('campanha/iniciar/', registerCampaign, name='iniciar_campanha'),
    path('campanha/listar/', getCampanhas, name='listar_campanhas'),
    path('campanha/ativa/', getCampanhasAtivas, name='listar_ativas'),
    path('campanha/encerrada/', getCampanhasEncerradas, name='listar_encerradas'),

    # Mapa
    path('mapa/exibir/', cadastrarPortoSeguro, name='exibir_mapa')

]
