from flask import Flask, request, jsonify

app = Flask(__name__)
usuarios = {}

@app.route('/register', methods=['POST'])
def cadastrar_usuario():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in usuarios:
        return jsonify({"message": "Usuário já existe!"}), 400
    usuarios[username] = password
    return jsonify({"message": "Usuário cadastrado com sucesso!"}), 200

@app.route('/login', methods=['POST'])
def login_usuario():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if usuarios.get(username) == password:
        return jsonify({"message": f"Bem-vindo, {username}!"}), 200
    return jsonify({"message": "Nome de usuário ou senha incorretos."}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
