from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuração do banco de dados SQLite


def criar_tabela():
    conn = sqlite3.connect("banco_de_dados.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS mensagens (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        mensagem TEXT
                    )''')
    conn.commit()
    conn.close()


criar_tabela()

# Rota da página inicial


@app.route('/')
def index():
    return render_template('index.html')

# Rota da página Sobre


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rota da página Nossos Trabalhos


@app.route('/nossos_trabalhos')
def nossos_trabalhos():
    return render_template('nossos_trabalhos.html')

# Rota da página Contato


@app.route('/contato')
def contato():
    return render_template('contato.html')

# Rota do formulário de Fale Conosco


@app.route('/fale_conosco', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']

        conn = sqlite3.connect("banco_de_dados.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mensagens (nome, email, mensagem) VALUES (?, ?, ?)", (nome, email, mensagem))
        conn.commit()
        conn.close()

        return redirect(url_for('fale_conosco'))

    return render_template('fale_conosco.html')


if __name__ == '__main__':
    app.run(debug=True)
