class Modelo:
    def __init__(self, nome, marca=None, categoria=None):
        self.id = None
        self.nome = nome[:80]
        self.marca = marca[:80] if marca else None
        self.categoria = categoria[:80] if categoria else None

    def __str__(self):
        if self.marca:
            return f"{self.marca.upper()}, {self.nome.upper()}"
        return self.nome.upper()