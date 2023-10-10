from flask import Flask, render_template, request, redirect, url_for
from SQLALCHEMY

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Mensagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    sobrenome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    celular = db.Column(db.String(20))
    telefone = db.Column(db.String(20))
    assunto = db.Column(db.String(255))
    mensagem = db.Column(db.Text)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/trabalhos')
def nossos_trabalhos():
    return render_template('trabalhos.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/faleconosco.html', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        celular = request.form['celular']
        telefone = request.form['telefone']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        nova_mensagem = Mensagem(nome=nome, sobrenome=sobrenome, email=email,
                                 celular=celular, telefone=telefone, assunto=assunto, mensagem=mensagem)
        db.session.add(nova_mensagem)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('fale_conosco.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
