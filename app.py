from flask import Flask, render_template, request, redirect, url_for
import models

app = Flask(__name__)

@app.route("/")
def index():
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


if __name__ == "__main__":
    app.run(debug=True)
