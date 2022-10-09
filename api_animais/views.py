
# Create your views here.
from rest_framework import viewsets, generics
from .models import Animal,Campanha, Usuario
from .serializers import AnimalSerializer, \
        CampanhaSerializer, UsuarioSerializer

from .permissions import AutorAlterarOuApenasLeitura

class AnimalViewSet(viewsets.ModelViewSet):
    permission_classes = (AutorAlterarOuApenasLeitura,)
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class CampanhaViewSet(viewsets.ModelViewSet):
    permission_classes = (AutorAlterarOuApenasLeitura,)
    queryset = Campanha.objects.all()
    serializer_class = CampanhaSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = (AutorAlterarOuApenasLeitura,)
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer

   