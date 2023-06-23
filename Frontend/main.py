
from Backend.core_helper import *
from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import signal, subprocess

app = Flask(__name__)
app.secret_key = b'\x9d\x97Leel\xe1\x15o\xd9:\xe8'
CORS(app)

class sveltekit():
    def run(self):
        os.chdir("Frontend")

        self.process = subprocess.Popen(
            ["npm", "run", "dev", "--", "--host"], 
            stdout=subprocess.DEVNULL, 
            shell=False
        ).pid

        os.chdir("../")

    def kill(self):
        os.killpg(os.getpgid(self.process), signal.SIGTERM)

def start_server():
    serve(app, host="localhost", port=5000)

@app.route("/api/version", methods=["GET"])
def version():
    return jsonify(version=Data.System.version, db_version=Data.Database.version)

