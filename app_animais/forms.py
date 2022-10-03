from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm

from api_animais.models import Usuario
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
        fields = ['email','username','first_name','last_name']