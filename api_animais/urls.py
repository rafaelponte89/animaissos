
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter
from .views import AnimalViewSet,CampanhaViewSet, UserViewSet

router = SimpleRouter()
router.register('usuarios',UserViewSet,basename='usuarios')
router.register('animais',AnimalViewSet, basename='animais')
router.register('campanhas',CampanhaViewSet, basename='campanhas')

urlpatterns = router.urls
