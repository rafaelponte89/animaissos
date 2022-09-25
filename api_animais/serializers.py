
from rest_framework import serializers
from .models import Animal, Campanha
from django.contrib.auth.models import User



class AnimalSerializer(serializers.ModelSerializer):


    class Meta:
        model = Animal
        fields = '__all__'

class CampanhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campanha
        fields = ('data_final','titulo','finalidade','username')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username','password','first_name','last_name')