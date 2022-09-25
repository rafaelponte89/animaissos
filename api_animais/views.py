from urllib import request


# Create your views here.
from rest_framework import viewsets
from .models import Animal,Campanha
from .serializers import AnimalSerializer, \
        CampanhaSerializer, UserSerializer
from django.contrib.auth.models import User

from .permissions import AutorAlterarOuApenasLeitura

from rest_framework.response import Response

from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status

from django.shortcuts import get_object_or_404

class AnimalViewSet(viewsets.ModelViewSet):

    permission_classes = (AutorAlterarOuApenasLeitura,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class CampanhaViewSet(viewsets.ModelViewSet):
    permission_classes = (AutorAlterarOuApenasLeitura,)
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer

class UserViewSet(viewsets.ModelViewSet):
    #permission_classes = (AutorAlterarOuApenasLeitura,)
    # queryset = User.objects.all()
    # serializer_class = UserSerializer
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

        
    def get_permissions(self):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]

        

        return [permission() for permission in permission_classes]