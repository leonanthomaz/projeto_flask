from flask import Flask

app = Flask(__name__)

@app.route("/")
def index ():
    return "Página principal - Teste"

app.run(port=5000)