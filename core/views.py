from rest_framework import viewsets
from .models import Acessorio, Cor, Modelo, Veiculo
from .serializers import *

class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class CorViewSet(viewsets.ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
