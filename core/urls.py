from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('acessorios', AcessorioViewSet)
router.register('cores', CorViewSet)
router.register('modelos', ModeloViewSet)
router.register('veiculos', VeiculoViewSet)

urlpatterns = router.urls
