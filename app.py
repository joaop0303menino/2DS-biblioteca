from flask import Flask, render_template
import integracao_sql as i_sql
from hashlib import sha256

cursor, conexao = i_sql.juncao_sql()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")

login = request.form['text']
senha = request.form['password']


@app.route('/pagina-main', methods=['POST'])
def home1():
    return 'd'

if __name__ == '__main__':
    app.run(debug=True)