from rest_framework import viewsets
from .serializer import *
from .models import *

class CategoriasViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasSerializer

class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = CarSerializer
