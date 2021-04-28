from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/v1.0/categorias',CategoriasViewset)
router.register('api/v1.0/vehiculos',VehiculoViewset)

urlpatterns = router.urls