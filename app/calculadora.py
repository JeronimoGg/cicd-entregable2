"""Módulo de funciones aritméticas básicas.

Contiene las operaciones fundamentales de la calculadora:
- Suma
- Resta
- Multiplicación
- División (con control de división por cero)
"""
def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a por b."""
    return a * b


def dividir(a, b):
    """Devuelve la división de a entre b.

    Lanza ZeroDivisionError si b es igual a 0.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
