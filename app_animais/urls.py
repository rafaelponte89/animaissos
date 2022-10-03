from django.urls.conf import path
from  .views import  register

from  django.contrib.auth import views as auth_views


urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',register, name='register'),
]