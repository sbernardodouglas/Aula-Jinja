import math
from flask import render_template, request

def calcular():
  
    try:
        num1 = float(request.form["num1"])
    except (ValueError, KeyError):
        return render_template(
            "calculadora.html",
            etapas="Erro: O primeiro número é obrigatório e deve ser válido.",
            resultados=""
        )

    operacao = request.form["operacao"]

    
    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro: número negativo"
            etapas = f"Não existe raiz real de ({num1})."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√({num1}) = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro: valor inválido"
            etapas = f"O logaritmo só está definido para números estritamente positivos. ({num1} <= 0)"
        else:
            resultado = math.log10(num1)
            etapas = f"log10({num1}) = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

   
    else:
        num2_valor = request.form.get("num2", "").strip()
        if not num2_valor:
            return render_template(
                "calculadora.html",
                etapas="Informe o segundo número para esta operação.",
                resultados=""
            )
        try:
            num2 = float(num2_valor)
        except ValueError:
            return render_template(
                "calculadora.html",
                etapas="Erro: O segundo número deve ser um valor válido.",
                resultados=""
            )

    
        if operacao == "+":
            resultado = num1 + num2
            etapas = f"({num1}) + ({num2}) = {resultado}"
        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"({num1}) - ({num2}) = {resultado}"
        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"({num1}) * ({num2}) = {resultado}"
        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro: divisão por zero"
                etapas = "Não é possível dividir por zero."
            else:
                resultado = num1 / num2
                etapas = f"({num1}) / ({num2}) = {resultado}"
        elif operacao == "**":
            try:
                resultado = num1 ** num2
                etapas = f"({num1}) ^ ({num2}) = {resultado}"
            except OverflowError:
                resultado = "Erro: transbordo"
                etapas = "O resultado desta potência é grande demais."
        else:
            resultado = "Erro: operação inválida"
            etapas = "Operação não reconhecida."

        return render_template("calculadora.html", etapas=etapas, resultados=resultado)