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
    # Campos apenas para leitura (mostram nomes bonitos no JSON)
    modelo_nome = serializers.CharField(source='modelo.nome', read_only=True)
    cor_nome = serializers.CharField(source='cor.nome', read_only=True)
    acessorios_nomes = serializers.StringRelatedField(
        source='acessorios', many=True, read_only=True
    )

    class Meta:
        model = Veiculo
        fields = [
            'id',
            'ano',
            'preco',
            'modelo',
            'modelo_nome',
            'cor',
            'cor_nome',
            'acessorios',
            'acessorios_nomes',
        ]