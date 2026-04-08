from rest_framework import serializers
from .models import Acessorio, Cor, Modelo, Veiculo

class AcessorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acessorio
        fields = '__all__'

class CorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'
