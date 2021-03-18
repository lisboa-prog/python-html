from flask import flask

app = Flask("microblog")

#aqui vai comentário
@app.route('/')
def index():
    return "Olá mundo"