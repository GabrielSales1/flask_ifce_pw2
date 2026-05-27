from flask import Flask, render_template, request
import math
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine
from models.Produto import Produto

from main import app
@app.route("/produtos/salvar", methods=["POST"])
def salvarProduto():
    msg = None
    prd = None
    try:
        session = Session()
        codigo = request.form.get("codigo")
        descricao = request.form.get("descricao")
        preco = request.form.get("preco")
        id = request.form.get("id");

        if id and id.strip():
            prd = session.query(Produto).filter(Produto.id == id).first();
        else:
            prd = Produto()
        prd.codigo = codigo.strip()
        prd.descricao = descricao.strip()
        
        
        if len(prd.codigo) > 20:
            raise ValueError("O código do produto deve conter no máximo 20 caracteres.")
        if len(prd.descricao) > 100:
            raise ValueError("A descrição do produto deve conter no máximo 100 caracteres.")
        try:
            prd.preco = float(preco)
        except ValueError:
            raise ValueError("O preço do produto deve ser um número válido.")
        session.add(prd)
        session.commit()
        return render_template("cadproduto.html",
        msg="Salvo com sucesso!", produto=Produto(codigo="", descricao="", preco=0.00))
    except ValueError as e:
        msg = e.args[0]
        prd.preco = preco
    return render_template("produtos/cadproduto.html", msg=msg, produto=prd)

@app.route("/listprodutos")
def listprodutos():
    session = Session()
    produtos = session.query(Produto).all()
    return render_template("produtos/listprodutos.html", 
    produtos=produtos, produto=Produto(codigo="", descricao="", preco=0.00))

@app.route("/pesquisarprodutos", methods=["GET"])
def pesquisarprodutos():
    
    session = Session()
    codigo = request.args.get("codigo").strip()
    descricao = request.args.get("descricao").strip()
    prd = Produto(codigo=codigo, descricao=descricao, preco=0.0)
    produtos = session.query(Produto).filter(Produto.codigo.contains(codigo) & Produto.descricao.contains(descricao)).all()
    return render_template("produtos/listprodutos.html", 
    produtos=produtos, produto=prd)



@app.route("/produto/update/<int:id>")
def update_produto(id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == id).first()
    return render_template("produtos/cadproduto.html", produto=produto)

@app.route("/cadprodutos")
def cadprodutos():
    return render_template("produtos/cadproduto.html", 
    produto=Produto(codigo="",descricao="", preco=0.0))

@app.route("/produto/delete/<int:id>" , methods=["GET"])
def delete_produto(id):
    session = Session()
    p = session.query(Produto).filter(Produto.id == id).first()
    session.delete(p)
    session.commit()
    return listprodutos()
