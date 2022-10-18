
from rest_framework import serializers
from .models import Animal, Campanha, Usuario


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'

class CampanhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campanha
        fields = ('data_inicial','data_final','titulo','informacoes','username')

class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style = {'input_type': 'password'},
        write_only = True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style = {'input_type':'password'},
        write_only = True,
        label= "Confirme a senha"
    )



    class Meta:
        model = Usuario
        fields = ('username','email','password','password_confirm')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        conta = Usuario(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta