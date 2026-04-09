class Acessorio:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao[:100]  # máximo 100 caracteres

    def __str__(self):
        return f"{self.id} - {self.descricao}"