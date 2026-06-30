from flask import Blueprint, redirect, render_template, request, url_for
from datetime import datetime

from models import Filme, Sala, Sessao, db


cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")

@cinema_bp.route("/")
def index():
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        sessao = Sessao(filme_id = int(request.form["filme_id"]), 
        data_hora=datetime.fromisoformat(request.form["data_hora"]),
        sala_id = int(request.form["sala_id"]),
        preco=float(request.form["preco"]),
        )
        db.session.add(sessao)
        db.session.commit()
        redirect("cinema/lista_sessoes.html")
        

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
