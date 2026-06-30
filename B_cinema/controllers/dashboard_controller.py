from flask import Blueprint, render_template
from models import Filme, Sala, Sessao

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def index():
    return  render_template("index.html",
    total_filme = Filme.query.count(),
    total_sala = Sala.query.count(),
    total_sessao = Sessao.query.count())

