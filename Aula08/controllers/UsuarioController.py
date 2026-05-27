from flask import Flask, render_template, request
import math
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine
from models.Usuario import Usuario

from main import app


@app.route("/user/new")
def new_user():
    return render_template("usuarios/newuser.html")

@app.route("/user/update/<int:id>")
def update_user(id):
    session = Session()
    user = session.query(Usuario).filter(Usuario.id == id).first()
    return render_template("usuarios/updateuser.html", user=user)

@app.route("/user/delete/<int:id>" , methods=["GET"])
def delete_user(id):
    session = Session()
    user = session.query(Usuario).filter(Usuario.id == id).first()
    session.delete(user)
    session.commit()
    return list_user(msg="Usuário deletado com sucesso!");


@app.route("/user/save", methods=["POST"])
def save_user():
    msg = None
    try:
        session = Session()
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        login = request.form.get("login")
        csenha = request.form.get("csenha")
        user = Usuario()
        user.nome = nome
        user.senha = senha
        user.login = login
        user.csenha = csenha
        validate_user_data(user)
        session.add(user)
        session.commit()
        msg = "Usuário cadastrado com sucesso!"
    
    except ValueError as e:
        msg = e.args[0]
    except DataError as e:
        msg = "Erro ao cadastrar usuário. Verifique os dados e tente novamente."
        session.rollback()
    except PendingRollbackError  as e:
        msg = "Erro ao cadastrar usuário. Verifique os dados e tente novamente."
    return render_template("usuarios/newuser.html", error=msg)
@app.route("/user/update", methods=["POST"])
def update_user_do():
    msg = None
    try:
        session = Session()
        id = request.form.get("id")
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        login = request.form.get("login")
        csenha = request.form.get("csenha")
        user = session.query(Usuario).filter(Usuario.id == id).first()
        if not user:
            raise ValueError("Usuário não encontrado.")
        user.nome = nome
        user.senha = senha
        user.login = login
        user.csenha = csenha
        validate_user_data(user)
        session.commit()
        return list_user(msg="Usuário atualizado com sucesso!");
    except ValueError as e:
        msg = e.args[0]
    except DataError as e:
        msg = "Erro de transação pendente. Realizando rollback."
        session.rollback()
    except PendingRollbackError  as e:
        msg = "Erro de transação pendente. Realizando rollback."
    return render_template("usuarios/updateuser.html", user=user, error=msg)

@app.route("/user/list")
def list_user(msg=None):
    list = Session().query(Usuario).all();
    return render_template("usuarios/userlist.html", list=list, msg=msg)

def validate_user_data(Usuario):
    if len(Usuario.login) > 20:
        raise ValueError("O login do usuário deve conter no máximo 20 caracteres.")
    if len(Usuario.senha) > 10:
        raise ValueError("A senha do usuário deve conter no máximo 10 caracteres.")
    if len(Usuario.nome) > 50:
        raise ValueError("O nome do usuário deve conter no máximo 50 caracteres.")
    if not Usuario.login.strip():
        raise ValueError("O login do usuário não pode ser vazio.")
    if not Usuario.senha.strip():
        raise ValueError("A senha do usuário não pode ser vazia.")
    if not Usuario.nome.strip():
        raise ValueError("O nome do usuário não pode ser vazio.")
    if Usuario.senha != Usuario.csenha:
        raise ValueError("A senha e a confirmação de senha devem ser iguais.")
    

