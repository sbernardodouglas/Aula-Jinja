from flask import Flask, render_template, request
import calculadora

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return calculadora.calcular()
    return render_template("calculadora.html", etapas=None, resultados="")

if __name__ == "__main__":
    app.run(debug=True)