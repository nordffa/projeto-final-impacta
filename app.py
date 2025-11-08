from flask import Flask, render_template, request, redirect, url_for, session
import models
from db import get_connection
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # chave segura para sessão


# ==============================
# LOGIN / LOGOUT
# ==============================
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["login"]
        senha = request.form["senha"]

        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM usuarios WHERE login=%s AND senha=%s", (usuario, senha))
            user = cur.fetchone()
            cur.close()
            conn.close()

            if user:
                session["usuario"] = usuario
                return redirect(url_for("index"))
            else:
                return render_template("login.html", error="Usuário ou senha inválidos.")
        else:
            return render_template("login.html", error="Erro ao conectar ao banco de dados.")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


# ==============================
# VERIFICADOR DE LOGIN
# ==============================
def login_required(func):
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "usuario" not in session:
            return redirect(url_for("login"))
        return func(*args, **kwargs)

    return wrapper


# ==============================
# PRODUTOS
# ==============================
@app.route("/index")
@login_required
def index():
    produtos = models.listar_produtos()
    return render_template("listar.html", produtos=produtos)


@app.route("/listar")
@login_required
def listar():
    produtos = models.listar_produtos()
    return render_template("listar.html", produtos=produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
@login_required
def cadastrar():
    if request.method == "POST":
        descricao = request.form["descricao"]
        valor_unitario = request.form["valor_unitario"]
        qtde_estoque = request.form["qtde_estoque"]
        fornecedor = request.form["fornecedor"]
        models.inserir_produto(descricao, valor_unitario, qtde_estoque, fornecedor)
        return redirect(url_for("index"))
    return render_template("cadastrar.html")


@app.route("/atualizar/<int:cod_produto>", methods=["POST"])
@login_required
def atualizar(cod_produto):
    nova_qtde = request.form["qtde_estoque"]
    models.atualizar_estoque(cod_produto, nova_qtde)
    return redirect(url_for("index"))


@app.route("/deletar/<int:cod_produto>", methods=["POST"])
@login_required
def deletar(cod_produto):
    models.desativar_produto(cod_produto)
    return redirect(url_for("index"))


# ==============================
# CLIENTES
# ==============================
@app.route("/clientes", methods=["GET", "POST"])
@login_required
def clientes():
    clientes = models.listar_clientes()
    return render_template("listar_cliente.html", clientes=clientes)


@app.route("/deletar_cliente/<int:cod_cliente>", methods=["POST"])
@login_required
def deletar_cliente(cod_cliente):
    models.desativar_cliente(cod_cliente)
    return redirect(url_for("clientes"))


@app.route("/cadastrar_cliente", methods=["GET", "POST"])
@login_required
def cadastrar_cliente():
    if request.method == "POST":
        nome_completo = request.form["nome_completo"]
        cpf = request.form["cpf"]
        models.inserir_cliente(nome_completo, cpf)
        return redirect(url_for("clientes"))
    return render_template("cadastrar_cliente.html")


# ==============================
# FORNECEDORES
# ==============================
@app.route("/fornecedores")
@login_required
def fornecedores():
    fornecedores = models.listar_fornecedores()
    return render_template("listar_fornecedores.html", fornecedores=fornecedores)


@app.route("/fornecedor/cadastrar", methods=["GET", "POST"])
@login_required
def fornecedor_cadastrar():
    if request.method == "POST":
        nome_fantasia = request.form["nome_fantasia"]
        razao_social = request.form["razao_social"]
        cnpj = request.form["cnpj"]

        models.inserir_fornecedor(nome_fantasia, razao_social, cnpj, True)
        return redirect(url_for("fornecedores"))
    return render_template("fornecedor_cadastrar.html")


@app.route("/fornecedor/deletar/<int:cod_fornecedor>", methods=["POST"])
@login_required
def deletar_fornecedor(cod_fornecedor):
    models.desativar_fornecedor(cod_fornecedor)
    return redirect(url_for("fornecedores"))


if __name__ == "__main__":
    app.run(debug=True)
