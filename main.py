import sqlite3
from produto import Produto


def conectar():
    conexao = sqlite3.connect("estoque.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    """)
    conexao.commit()
    return conexao, cursor


def adicionar_produto(cursor, conexao, nome, preco, quantidade):
    cursor.execute(
        "INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)",
        (nome, preco, quantidade)
    )
    conexao.commit()
    print(f"Produto '{nome}' adicionado com sucesso!")


def listar_produtos(cursor):
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    if not produtos:
        print("Estoque vazio.")
        return
    for p in produtos:
        produto = Produto(*p)
        print(produto)


def vender_produto(cursor, conexao, id, quantidade_vendida):
    cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (id,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Produto não encontrado.")
        return

    estoque_atual = resultado[0]
    if quantidade_vendida > estoque_atual:
        print("Estoque insuficiente!")
        return

    novo_estoque = estoque_atual - quantidade_vendida
    cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (novo_estoque, id))
    conexao.commit()
    print(f"Venda realizada! Estoque atualizado: {novo_estoque}")


def menu():
    conexao, cursor = conectar()

    while True:
        print("\n--- SISTEMA DE ESTOQUE ---")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Vender produto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(cursor, conexao, nome, preco, quantidade)

        elif opcao == "2":
            listar_produtos(cursor)

        elif opcao == "3":
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade vendida: "))
            vender_produto(cursor, conexao, id, quantidade)

        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

    conexao.close()


if __name__ == "__main__":
    menu()
