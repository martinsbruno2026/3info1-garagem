from rest_framework import viewsets

from ..models import Acessorio
from ..serializers import AcessorioSerializer


class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer