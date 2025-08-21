from db import get_connection

# Inserir produto
def inserir_produto(descricao, valor_unitario, qtde_estoque, fornecedor):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO produto (descricao, valor_unitario, qtde_estoque, fornecedor) VALUES (%s, %s, %s, %s)",
            (descricao, valor_unitario, qtde_estoque, fornecedor)
        )
        conn.commit()
        cur.close()
        conn.close()

# Listar produtos
def listar_produtos():
    conn = get_connection()
    produtos = []
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM produto ORDER BY cod_produto")
        produtos = cur.fetchall()
        cur.close()
        conn.close()
    return produtos

# Atualizar estoque
def atualizar_estoque(cod_produto, nova_qtde):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE produto SET qtde_estoque = %s WHERE cod_produto = %s",
            (nova_qtde, cod_produto)
        )
        conn.commit()
        cur.close()
        conn.close()
