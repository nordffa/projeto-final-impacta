from db import get_connection


def inserir_produto(descricao, valor_unitario, qtde_estoque, fornecedor, ativo="TRUE"):
    """
    Funcao que insere produtos no banco de dados
    """
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO produto (descricao, valor_unitario, qtde_estoque, fornecedor, ativo) VALUES (%s, %s, %s, %s, %s)",
            (descricao, valor_unitario, qtde_estoque, fornecedor, ativo),
        )
        conn.commit()
        cur.close()
        conn.close()


def listar_produtos():
    """
    Funcao que lista todos os produtos do estoque
    """
    conn = get_connection()
    produtos = []
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM produto WHERE ativo = TRUE ORDER BY cod_produto")
        produtos = cur.fetchall()
        cur.close()
        conn.close()
    return produtos


def atualizar_estoque(cod_produto, nova_qtde):
    """
    Funcao que atualiza a quantidade do produto
    """
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE produto SET qtde_estoque = %s WHERE cod_produto = %s",
            (nova_qtde, cod_produto),
        )
        conn.commit()
        cur.close()
        conn.close()


def desativar_produto(cod_produto):
    """
    Funcao que muda o status do produto para "FALSE" e remove da visualizacao de todos os produtos
    """
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE produto SET ativo = FALSE WHERE cod_produto = %s", (cod_produto,)
        )
        conn.commit()
        cur.close()
        conn.close()


def inserir_cliente(nome_completo, cpf, ativo="TRUE"):
    """
    Funcao que insere um cliente no banco de dados
    """
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO cliente (nome_completo, cpf, ativo) VALUES (%s, %s, %s)",
            (nome_completo, cpf, ativo),
        )
        conn.commit()
        cur.close()
        conn.close()


def listar_clientes():
    """
    Funcao que lista todos os clientes cadastrados
    """
    conn = get_connection()
    produtos = []
    if conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM cliente WHERE ativo = TRUE ORDER BY cod_cliente")
        produtos = cur.fetchall()
        cur.close()
        conn.close()
    return produtos


def desativar_cliente(cod_cliente):
    """
    Funcao que muda o status do cliente para "FALSE" e remove da visualizacao de todos os clientes
    """
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE cliente SET ativo = FALSE WHERE cod_cliente = %s", (cod_cliente,)
        )
        conn.commit()
        cur.close()
        conn.close()
