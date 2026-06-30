class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f"[{self.id}] {self.nome} - R${self.preco:.2f} (qtd: {self.quantidade})"
