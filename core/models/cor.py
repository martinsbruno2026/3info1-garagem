class Cor:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome[:40]  # Limita a 40 caracteres

    def __str__(self):
        return f"{self.nome} (ID: {self.id})"
    def __repr__(self):
        return f"Cor(id={self.id}, nome='{self.nome}')"