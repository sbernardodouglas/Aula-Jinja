from flask import Flask, request, render_template_string

app = Flask(__name__)

usuarios = {
    "Bernardo": "22300856",
    "dolga": "cotemig2026",
    "janaina": "cotemig2026",
    "antonio": "cotemig2026"
}

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>

        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>

            <input type="password" name="senha" placeholder="Senha"><br><br>

            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    for nome, senha_correta in usuarios.items():

        if usuario == nome and senha == senha_correta:
            return f"<h1>Bem-vindo, {usuario}!</h1>"

    return "<h1>Login inválido</h1>"

@app.route('/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        return do_the_login()

    return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)