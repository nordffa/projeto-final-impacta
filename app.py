from flask import Flask, render_template, request, redirect, url_for
import models

app = Flask(__name__)

@app.route("/")
def index():
    produtos = models.listar_produtos()
    return render_template("listar.html", produtos=produtos)


@app.route("/listar")
def listar():
    produtos = models.listar_produtos()
    return render_template("listar.html", produtos=produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
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
def atualizar(cod_produto):
    nova_qtde = request.form["qtde_estoque"]
    models.atualizar_estoque(cod_produto, nova_qtde)
    return redirect(url_for("index"))


@app.route("/deletar/<int:cod_produto>", methods=["POST"])
def deletar(cod_produto):
    models.desativar_produto(cod_produto)
    return redirect(url_for("index"))


# CLIENTES

@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    clientes = models.listar_clientes()
    return render_template("listar_cliente.html", clientes=clientes)


@app.route("/deletar_cliente/<int:cod_cliente>", methods=["POST"])
def deletar_cliente(cod_cliente):
    models.desativar_cliente(cod_cliente)
    return redirect(url_for("clientes"))


@app.route("/cadastrar_cliente", methods=["GET", "POST"])
def cadastrar_cliente():
    if request.method == "POST":
        nome_completo = request.form["nome_completo"]
        cpf = request.form["cpf"]
        models.inserir_cliente(nome_completo, cpf)
        return redirect(url_for("clientes"))
    return render_template("cadastrar_cliente.html")


# FORNECEDOR

@app.route("/fornecedor/cadastrar", methods=["GET", "POST"])
def fornecedor_cadastrar():
    if request.method == "POST":
        nome_fantasia = request.form["nome_fantasia"]
        razao_social = request.form["razao_social"]
        cnpj = request.form["cnpj"]
        return redirect(url_for("index"))
    return render_template("fornecedor_cadastrar.html")


@app.route("/fornecedores", methods=["GET", "POST"])
def fornecedores():
    fornecedores = models.listar_fornecedores()
    return render_template("listar_fornecedores.html", fornecedores=fornecedores)


if __name__ == "__main__":
    app.run(debug=True)
