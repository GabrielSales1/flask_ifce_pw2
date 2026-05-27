from flask import Flask, render_template, request
import math
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine
from models.TipoProduto import TipoProduto

from main import app
@app.route("/tipoprodutos/salvar", methods=["POST"])
def salvarTProduto():
    msg = None
    prd = None
    try:
        session = Session()
        descricao = request.form.get("descricao")
        id = request.form.get("id");
        if id and id.strip():
            prd = session.query(TipoProduto).filter(TipoProduto.id == id).first();
        else:
            prd = TipoProduto()
        prd.descricao = descricao.strip()
        
        
        if len(prd.descricao) > 100:
            raise ValueError("A descrição do produto deve conter no máximo 100 caracteres.")
        session.add(prd)
        session.commit()
        return listtipoprodutos();
        
    except ValueError as e:
        msg = e.args[0]
       
    return listtipoprodutos();

@app.route("/tipoprodutos/list")
def listtipoprodutos():
    session = Session()
    produtos = session.query(TipoProduto).all()
    return render_template("tipoProduto/list.html", 
    produtos=produtos, produto=TipoProduto(descricao=""))

@app.route("/tipoprodutos/pesquisar", methods=["GET"])
def pesquisatipoprodutos():
    
    session = Session()
    descricao = request.args.get("descricao").strip()
    prd = TipoProduto(descricao=descricao)
    produtos = session.query(TipoProduto).filter(TipoProduto.descricao.contains(descricao)).all()
    return render_template("tipoProduto/list.html", 
    produtos=produtos, produto=prd)



@app.route("/tipoproduto/update/<int:id>")
def update_tipoproduto(id):
    session = Session()
    tipoproduto = session.query(TipoProduto).filter(TipoProduto.id == id).first()
    return render_template("produtos/cadproduto.html", produto=tipoproduto)

@app.route("/tipoprodutos/new")
def cadtipoprodutos():
    return render_template("tipoProduto/cad.html", 
    produto=TipoProduto(descricao=""))

@app.route("/tipoproduto/delete/<int:id>" , methods=["GET"])
def delete_tipoproduto(id):
    session = Session()
    p = session.query(TipoProduto).filter(TipoProduto.id == id).first()
    session.delete(p)
    session.commit()
    return listprodutos()
