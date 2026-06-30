import math

from flask import (
    Blueprint,
    render_template,
    request
)

from models import Operacao

calculadora_bp = Blueprint(
    "calculadora",
    __name__
)


@calculadora_bp.route(
    "/",
    methods=["GET", "POST"]
)
def index():

    if request.method == "POST":
        return calcular()

    return render_template(
        "calculadora.html",
        etapas="",
        resultados="",
        historico=Operacao.listar_recentes()
    )


def calcular():

    try:

        num1 = float(request.form["num1"])
        operacao = request.form["operacao"]

        resultado = ""
        etapas = ""
        num2 = None

        if operacao == "sqrt":

            if num1 < 0:
                resultado = "Erro"
                etapas = "Não existe raiz real para número negativo."

            else:
                resultado = math.sqrt(num1)
                etapas = f"√{num1} = {resultado}"

        else:

            valor_num2 = request.form.get(
                "num2",
                ""
            ).strip()

            if valor_num2 == "":
                return render_template(
                    "calculadora.html",
                    etapas="Informe o segundo número.",
                    resultados="",
                    historico=Operacao.listar_recentes()
                )

            num2 = float(valor_num2)

            if operacao == "+":
                resultado = num1 + num2
                etapas = f"{num1} + {num2} = {resultado}"

            elif operacao == "-":
                resultado = num1 - num2
                etapas = f"{num1} - {num2} = {resultado}"

            elif operacao == "*":
                resultado = num1 * num2
                etapas = f"{num1} * {num2} = {resultado}"

            elif operacao == "/":

                if num2 == 0:
                    resultado = "Erro"
                    etapas = "Não é possível dividir por zero."

                else:
                    resultado = num1 / num2
                    etapas = f"{num1} / {num2} = {resultado}"

            elif operacao == "**":
                resultado = num1 ** num2
                etapas = f"{num1} ** {num2} = {resultado}"

            else:
                resultado = "Erro"
                etapas = "Operação inválida."

        Operacao.salvar(
            num1,
            num2,
            operacao,
            etapas,
            resultado
        )

        return render_template(
            "calculadora.html",
            etapas=etapas,
            resultados=resultado,
            historico=Operacao.listar_recentes()
        )

    except Exception as erro:

        return render_template(
            "calculadora.html",
            etapas=f"Erro: {erro}",
            resultados="",
            historico=Operacao.listar_recentes()
        )