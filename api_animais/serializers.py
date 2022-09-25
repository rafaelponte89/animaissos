from dataclasses import fields
from rest_framework import serializers
from .models import Animal, Campanha




class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'

class CampanhaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campanha
        read_only_fields = ['data_inicial','ativa']