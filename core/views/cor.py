from rest_framework import viewsets

from ..models import Cor
from ..serializers import CorSerializer


class CorViewSet(viewsets.ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer