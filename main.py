from flask import Flask, render_template, request, redirect

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

# FLASK
app = Flask(__name__)

# BANCO
engine = create_engine("mysql+pymysql://root:@localhost:3306/pw2")

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

# MODEL
class Cliente(Base):

    __tablename__ = "clientes"

    id = Column(
        Integer,
        primary_key=True
    )

    nome = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(100),
        nullable=False
    )

    telefone = Column(
        String(20),
        nullable=False
    )

Base.metadata.create_all(engine)

@app.route("/")
def home():

    return redirect("/clientes")

@app.route("/clientes")
def clientes():

    lista_clientes = session.query(Cliente).all()

    return render_template(
        "clientes.html",
        clientes=lista_clientes
    )

@app.route("/clientes/inserir", methods=["GET", "POST"])
def inserir_cliente():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]

        novo_cliente = Cliente(
            nome=nome,
            email=email,
            telefone=telefone
        )

        session.add(novo_cliente)

        session.commit()

        return redirect("/clientes")

    return render_template("inserir_cliente.html")

@app.route("/clientes/editar/<int:id>", methods=["GET", "POST"])
def editar_cliente(id):

    cliente = session.query(Cliente).filter_by(id=id).first()

    if request.method == "POST":

        cliente.nome = request.form["nome"]
        cliente.email = request.form["email"]
        cliente.telefone = request.form["telefone"]

        session.commit()

        return redirect("/clientes")

    return render_template(
        "editar_cliente.html",
        cliente=cliente
    )

@app.route("/clientes/apagar/<int:id>")
def apagar_cliente(id):

    cliente = session.query(Cliente).filter_by(id=id).first()

    session.delete(cliente)

    session.commit()

    return redirect("/clientes")

@app.route("/clientes/procurar", methods=["GET", "POST"])
def procurar_cliente():

    clientes = []

    if request.method == "POST":

        nome = request.form["nome"]

        clientes = session.query(Cliente).filter(
            Cliente.nome.like(f"%{nome}%")
        ).all()

    return render_template(
        "procurar_cliente.html",
        clientes=clientes
    )

if __name__ == "__main__":
    app.run(debug=True)