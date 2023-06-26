
from Backend.core_helper import *
from Backend.Database.database import db
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
app.secret_key = b'\x9d\x97Leel\xe1\x15o\xd9:\xe8'
CORS(app)

def flask_task():
    serve(app, host="0.0.0.0", port=5002)

@app.route("/api/status", methods=["GET"])
def status():
    return jsonify(status="ok")

@app.route("/api/version", methods=["GET"])
def version():
    return jsonify(version=Data.System.version, db_version=Data.Database.version)

@app.route("/api/user/auth/login", methods=["POST"])
def user_auth_login():
    request_data = request.get_json()

    lang = request_data["lang"]
    session_token = request_data["session_token"]

    if not lang or not session_token:
        return jsonify(error="invalid_request")
    
    user = db.User.login(lang, session_token)
    if user[0] == 200:
        return jsonify(user={
            "id": user[1].id,
            "name": user[1].name,
            "username": user[1].username,
            "email": user[1].email,
            "password": user[1].password,
            "updated_at": user[1].updated_at,
            "created_at": user[1].created_at
        })
    
    return jsonify(error=user[0], message=user[1])

@app.route("/api/user/auth/sign_in", methods=["POST"])
def user_auth_sign_in():
    request_data = request.get_json()

    lang = request_data["lang"]
    username_or_email = request_data["username_or_email"]
    password = request_data["password"]

    if not lang or not username_or_email or not password:
        return jsonify(error="invalid_request")
    
    session_token = db.User.sign_in(lang, username_or_email, password)
    if session_token[0] == 200:
        return jsonify(session_token=session_token[1])
    
    return jsonify(error=session_token[0], message=session_token[1])

@app.route("/api/user/auth/register", methods=["POST"])
def user_auth_register():
    request_data = request.get_json()

    lang = request_data["lang"]
    name = request_data["name"]
    username = request_data["username"]
    email = request_data["email"]
    password = request_data["password"]

    if not lang or not username or not name or not email or not password:
        return jsonify(error="invalid_request")
    
    user = db.User.create(lang, name, username, email, password)

    if user[0] == 200:
        session_token = db.User.sign_in(lang, username, password)
        if session_token[0] == 200:
            return jsonify(session_token=session_token[1])
        else:
            return jsonify(error=session_token[0], message=session_token[1])
    
    return jsonify(error=user[0], message=user[1])