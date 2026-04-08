
from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.descricao}"


class Cor(models.Model):
    nome = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.nome} ({self.id})"


class Modelo(models.Model):
    nome = models.CharField(max_length=80)
    marca = models.CharField(max_length=80, blank=True, null=True)
    categoria = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.marca.upper() if self.marca else ''} {self.nome.upper()}"


class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio)

    def __str__(self):
        return f"{self.id} - {self.modelo} - {self.cor} - {self.ano}"
