CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS produto (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
descricao TEXT NOT NULL,
preco REAL NOT NULL,
quantidade INTEGER NOT NULL)
"""


INSERIR_PRODUTO = """
INSERT INTO produto (nome, descricao, preco, quantidade)
VALUES (?, ?, ?, ?)
"""


OBTER_TODOS = """
SELECT
id, nome, descricao, preco, quantidade
FROM produto
"""

