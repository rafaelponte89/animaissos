from django.urls.conf import path
from  .views import  register, perfil, registerAnimal, registerCampaign, update, getAnimais, getCampanhas
    

from  django.contrib.auth import views as auth_views


urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('perfil/<int:pk>', perfil, name='perfil'),
    path('perfil/update/', update, name='update'),
    path('register/',register, name='register'),
    path('cadastrarcampanha/', registerCampaign, name='iniciar_campanha'),
    path('cadastraranimais/', registerAnimal, name = 'cadastrar_animais'),
    path('listaranimais/', getAnimais, name = 'listar_animais'),
    path('listarcampanhas/', getCampanhas, name = 'listar_campanhas')
]