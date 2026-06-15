from flask import Flask, render_template, request
import math
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine
from models.Usuario import Usuario
from models.Cliente import Cliente
from models.Produto import Produto
from models.TipoProduto import TipoProduto

Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    session = Session()
    a = request.form.get("nome")
    b = request.form.get("senha")
    user = session.query(Usuario).filter(Usuario.login==a,
     Usuario.senha==b).first()
    print(user)
    if user:
        return render_template("dashboard.html")
    else:
        return render_template("index.html", error="Credenciais inválidas")

from controllers.UsuarioController import *  
from controllers.ProdutoController import *
from controllers.TipoProdutoController import *
from controllers.ClienteController import *
from controllers.api_produtos import *
from controllers.api_admins import *

if ( __name__ == "__main__"):
    app.run(debug=True, port=5001)