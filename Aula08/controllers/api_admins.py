from flask import request, jsonify
from main import app
from models.AdminDAO import AdminDAO

repo = AdminDAO()

@app.route('/api/admins', methods=['GET'])
def api_list_admins():
    return jsonify(repo.list_all())

@app.route('/api/admins', methods=['POST'])
def api_create_admin():
    data = request.get_json() or {}
    admin = repo.add(data)
    return jsonify(admin), 201

@app.route('/api/admins/<int:id>', methods=['GET'])
def api_get_admin(id):
    a = repo.get(id)
    if not a:
        return jsonify({'error':'Not found'}), 404
    return jsonify(a)

@app.route('/api/admins/<int:id>', methods=['PUT'])
def api_update_admin(id):
    data = request.get_json() or {}
    a = repo.update(id, data)
    if not a:
        return jsonify({'error':'Not found'}), 404
    return jsonify(a)

@app.route('/api/admins/<int:id>', methods=['DELETE'])
def api_delete_admin(id):
    ok = repo.delete(id)
    if not ok:
        return jsonify({'error':'Not found'}), 404
    return jsonify({'result':'deleted'})
