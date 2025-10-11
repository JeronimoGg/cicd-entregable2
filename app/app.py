"""Aplicación Flask de calculadora básica.

Este módulo define la aplicación web principal que permite realizar 
operaciones aritméticas simples (suma, resta, multiplicación y división) 
a través de un formulario HTML. 
Utiliza funciones definidas en `calculadora.py` para ejecutar las operaciones.
"""
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Vista principal de la aplicación.

    Muestra un formulario donde el usuario puede ingresar dos números
    y seleccionar una operación aritmética. Al enviar el formulario,
    se calcula el resultado y se muestra en la página.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(debug=True, port=5000, host="0.0.0.0")  # Quita debug=True para producción
