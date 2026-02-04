from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import auth, storage

app = Flask(__name__)
load_dotenv()

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

# Página de adicionar password
@app.route("/adicionar")
def adicionar_page():
    return render_template("adicionar.html")

# Página de ver passwords
@app.route("/ver")
def ver_page():
    return render_template("ver.html")

# API - Adicionar password
@app.route("/api/adicionar", methods=["POST"])
def api_adicionar():
    data = request.get_json()
    site = data.get("site")
    username = data.get("username")
    password = data.get("password")
    
    if not site or not username or not password:
        return jsonify({"error": "Dados em falta"}), 400
    
    storage.InserirDados(site, username, auth.cifrar_password(password))
    return jsonify({"message": "Password adicionada com sucesso"}), 201

# API - Ver passwords
@app.route("/api/ver", methods=["POST"])
def api_ver():
    data = request.get_json()
    master_password = data.get("master_password")
    site = data.get("site")
    
    if not master_password or not site:
        return jsonify({"error": "Dados em falta"}), 400
    
    if master_password != os.getenv('master_password'):
        return jsonify({"error": "Password mestra incorreta"}), 403
    
    passwords = storage.verPasswords(site)
    return jsonify({"passwords": passwords}), 200

if __name__ == "__main__":
    app.run(debug=True)