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


@app.route("/fornecedor/cadastrar", methods=["GET", "POST"])
def fornecedor_cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        cnpj = request.form["cpf"]        
        return redirect(url_for("index"))
    return render_template("fornecedor_cadastrar.html")

@app.route("/atualizar/<int:cod_produto>", methods=["POST"])
def atualizar(cod_produto):
    nova_qtde = request.form["qtde_estoque"]
    models.atualizar_estoque(cod_produto, nova_qtde)
    return redirect(url_for("index"))


@app.route("/deletar/<int:cod_produto>", methods=["POST"])
def deletar(cod_produto):
    models.desativar_produto(cod_produto)
    return redirect(url_for("index"))


@app.route("/clientes", methods=["GET", "POST"])
def clientes():
    clientes = models.listar_clientes()
    return render_template("listar_cliente.html", clientes=clientes)


@app.route("/atualizar_cliente/<int:cod_cliente>", methods=["POST"])
def atualizar_cliente(cod_cliente):
    pass


@app.route("/deletar_cliente/<int:cod_cliente>", methods=["POST"])
def deletar_cliente(cod_cliente):
    pass


if __name__ == "__main__":
    app.run(debug=True)
