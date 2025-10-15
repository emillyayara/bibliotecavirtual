from flask import *

app = Flask(__name__)
app.secret_key = 'b.emilly123.5/'
cad = ['clara,clara@gmail,99','emilly,emilly@gmail,77']
livros = []
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


@app.route('/cadlivro', methods=['POST'])
def cadastro_livro():
    global livros
    nomelivro = request.form.get('nomelivro')
    autor = request.form.get('autor')
    livro_novo = [nomelivro, autor]

    if livro_novo not in livros:
        livros.append(livro_novo)
        return "Livro cadastrado com sucesso!"
    else:
        return "Este livro já está cadastrado."




@app.route('/removlivros', methods=['GET', 'POST'])
def remover_livro():
    global livros
    mensagem = ''
    if request.method == 'POST':
        nomelivros = request.form.get('nome')
        if nomelivros in livros:
            livros.remove(nomelivros)
            mensagem = "Livro removido com sucesso!"
            return render_template('admin/removlivros.html', mensagem=mensagem)

        else:
            mensagem = 'Livro não encontrado!'
    return render_template('admin/removlivros.html', mensagem=mensagem)


@app.route('/listalivros', methods=['get'])
def listar_livros():
    if len(livros) > 0:
        return render_template('admin/listalivros.html', lista=livros, livros=livros)
    else:
        return render_template('admin/listalivros.html',  livros=livros)



@app.route('/pag_cadastro')
def pag_cadastro():
    return render_template('cadastro.html')

@app.route('/administrador', methods=['post'])
def administrador():
    senhadig = request.form.get('senha')

    if senhadig == senha:
        session['login'] = 'admin'
        return render_template('admin/pagiframe.html')

    else:
        return render_template('admin/admin.html')

@app.route('/pag_admin')
def pag_admin():
    return render_template('admin.html')
@app.route('/cadlivros')
def cadlivros():
    if session.get('login') == "admin":
      return render_template('admin/cadlivros.html')
    else:
        return 'Você não tem autorização'


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