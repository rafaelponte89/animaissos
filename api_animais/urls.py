
from django.conf import settings


from rest_framework.routers import SimpleRouter
from .views import AnimalViewSet,CampanhaViewSet, UsuarioViewSet

router = SimpleRouter()

router.register('animais',AnimalViewSet, basename='animais')
router.register('campanhas',CampanhaViewSet, basename='campanhas')
router.register('usuarios',UsuarioViewSet, basename='usuarios')

rotas = router.urls

urlpatterns =  rotas