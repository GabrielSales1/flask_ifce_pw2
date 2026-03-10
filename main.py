from flask import Flask,render_template,url_for

app = Flask(__name__)
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/fornecedores")
def fornecedores():
    return render_template("fornecedores.html")

@app.route("/vendas")
def vendas():
    return render_template("vendas.html")

if __name__ == '__main__':
    app.run(debug=True)