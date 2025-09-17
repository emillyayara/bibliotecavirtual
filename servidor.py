from flask import *

app = Flask(__name__)
cad = ['clara,clara@gmail,99','emilly,emilly@gmail,77']
log = []
senha = "123"


@app.route('/')
def inicio():
   return render_template('paginicial.html')

@app.route('/cadastro', methods=['post'])
def cadastro():
    global cad
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        confirma = request.form.get('confirmacao')
        if confirma == senha:
            cad.append([nome, email, senha])

            return render_template('paginicial.html')
        else:
            return render_template('paginicial.html')

@app.route('/pag_cadastro')
def pag_cadastro():
    return render_template('cadastro.html')

@app.route('/administrador', methods=['post'])
def administrador():
    senhadig = request.form.get('senha')
    if senhadig == senha:
        return render_template('cadlivros.html')

    else:
        return render_template('admin.html')

@app.route('/pag_admin')
def pag_admin():
    return render_template('admin.html')

@app.route('/logar', methods=['post'])
def logar():
    global log
    if request.method == 'POST':
        senha = request.form.get('senha')
        email = request.form.get('email')
        achei = False
        for usuario in cad:
            if usuario[1] == email and usuario[2] == senha:
                achei = True

        if achei:
            print('achou')
            return render_template('exposicao.html')
        else:
            print('errou')
            erro = ('você digitou email ou senha incorretos')
            return render_template('login.html', msg=erro)

@app.route('/pag_login')
def pag_login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)