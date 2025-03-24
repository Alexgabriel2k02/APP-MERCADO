from flask import Blueprint, request, jsonify

app = Blueprint('app', __name__)

users = []
products = []

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({"message": "Usuário cadastrado com sucesso!"})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            return jsonify({"message": "Login realizado com sucesso!"})
    return jsonify({"message": "Usuário ou senha inválidos!"}), 401

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.json
    products.append(data)
    return jsonify({"message": "Produto cadastrado com sucesso!"})

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)