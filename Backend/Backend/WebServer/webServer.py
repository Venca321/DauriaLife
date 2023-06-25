
from Backend.core_helper import *
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

