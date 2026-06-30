# sistema-estoque
=======
# 📦 Sistema de Gerenciamento de Estoque

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey?logo=sqlite)
![Status](https://img.shields.io/badge/status-concluído-success)

Sistema de linha de comando (CLI) para gerenciamento de estoque de uma loja, desenvolvido em Python com persistência de dados em banco SQLite. Permite cadastrar produtos, controlar quantidades e registrar vendas com atualização automática do estoque.

## 🎯 Funcionalidades

- ✅ Cadastro de produtos (nome, preço, quantidade)
- ✅ Listagem de todos os produtos em estoque
- ✅ Registro de vendas com baixa automática no estoque
- ✅ Validação de estoque insuficiente
- ✅ Persistência de dados em banco SQLite (os dados não se perdem ao fechar o programa)

## 🛠️ Tecnologias utilizadas

- **Python 3** — lógica do sistema
- **SQLite3** — banco de dados local
- **POO (Programação Orientada a Objetos)** — modelagem da entidade `Produto`

## 📂 Estrutura do projeto

```
sistema-estoque/
├── main.py          # ponto de entrada e lógica do sistema (CRUD + menu)
├── produto.py        # classe Produto (modelo de dados)
├── estoque.db         # banco de dados SQLite (gerado automaticamente)
└── README.md
```

## 🚀 Como executar

### Pré-requisitos
- Python 3.10 ou superior instalado ([download aqui](https://www.python.org/downloads/))

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/sistema-estoque.git

# Entre na pasta
cd sistema-estoque

# Execute o programa
python main.py
```

O banco de dados (`estoque.db`) é criado automaticamente na primeira execução.

## 💻 Exemplo de uso

```
--- SISTEMA DE ESTOQUE ---
1. Adicionar produto
2. Listar produtos
3. Vender produto
4. Sair
Escolha uma opção: 1
Nome do produto: Caneta Azul
Preço: 2.50
Quantidade: 50
Produto 'Caneta Azul' adicionado com sucesso!
```

## 🧠 O que esse projeto demonstra

Este projeto foi construído para praticar e demonstrar:

- Modelagem de dados com **classes em Python**
- Operações **CRUD** (Create, Read, Update) com **SQL**
- Uso de `sqlite3` nativo do Python (sem dependências externas)
- Prevenção de **SQL Injection** com queries parametrizadas (`?`)
- Organização de código em múltiplos arquivos (separação de responsabilidades)

## 🔮 Possíveis melhorias futuras

- [ ] Adicionar exclusão e edição de produtos
- [ ] Criar relatório de produtos com estoque baixo
- [ ] Migrar para interface web com Flask
- [ ] Adicionar testes automatizados

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar e modificar.

---

Desenvolvido como parte dos meus estudos em Python e bancos de dados. 🐍
>>>>>>> a05b789 (primeiro commit: sistema de estoque completo)
