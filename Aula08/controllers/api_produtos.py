from flask import request, jsonify
from main import app
from models.ProdutoRepository import ProdutoRepository

repo = ProdutoRepository()

@app.route('/api/produtos', methods=['GET'])
def api_list_produtos():
    return jsonify(repo.list_all())

@app.route('/api/produtos', methods=['POST'])
def api_create_produto():
    data = request.get_json() or {}
    prod = repo.add(data)
    return jsonify(prod), 201

@app.route('/api/produtos/<int:id>', methods=['GET'])
def api_get_produto(id):
    p = repo.get(id)
    if not p:
        return jsonify({'error':'Not found'}), 404
    return jsonify(p)

@app.route('/api/produtos/<int:id>', methods=['PUT'])
def api_update_produto(id):
    data = request.get_json() or {}
    p = repo.update(id, data)
    if not p:
        return jsonify({'error':'Not found'}), 404
    return jsonify(p)

@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def api_delete_produto(id):
    ok = repo.delete(id)
    if not ok:
        return jsonify({'error':'Not found'}), 404
    return jsonify({'result':'deleted'})
