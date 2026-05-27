from flask import render_template, request, url_for,redirect
from main import app
from models.Geral import Session
from models.Cliente import *

@app.route('/clientes/cadastro', methods=['GET'])
def cadCliente():
    db = Session()
    if request.method == 'GET':
        return render_template("cliente/cad_cliente.html")

@app.route('/clientes/cadastro/salvar', methods=['GET','POST'])
def salvarCliente():
    db = Session()
    if request.method == 'GET':
        return render_template("cliente/cad_cliente.html")
    
    if request.method == 'POST':
        nome = request.form.get("nome")
        email = request.form.get("email")
        endereco = request.form.get("endereco")
        telefone = request.form.get("telefone")

        clientes = Cliente(
            nome=nome,
            email=email,
            endereco=endereco,
            telefone=telefone
        )
        db.add(clientes)
        db.commit()
        return redirect(url_for('listaCliente'))

@app.route('/cliente/lista')
def listaCliente():
    db = Session()
    clientes = db.query(Cliente).all()
    return render_template('cliente/list_cliente.html', clientes=clientes)

@app.route("/cliente/delete/<int:id>" , methods=["GET"])
def delete_cliente(id):
    db = Session()
    c = db.query(Cliente).filter(Cliente.id == id).first()
    db.delete(c)
    db.commit()
    return listaCliente()

@app.route("/cliente/update/<int:id>")
def update_cliente(id):
    session = Session()
    cliente = session.query(Cliente).filter(Cliente.id == id).first()
    return render_template("cliente/update_cliente.html", c=cliente)

@app.route('/clientes/update/alterar', methods=['POST'])
def salvarAlterar():
    db = Session()
    cliente_id = request.form.get("id")

    if cliente_id:
        cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        
        if cliente:
            cliente.nome = request.form.get("nome")
            cliente.email = request.form.get("email")
            cliente.endereco = request.form.get("endereco")
            cliente.telefone = request.form.get("telefone")
            
            db.commit()
        return redirect(url_for('listaCliente'))



