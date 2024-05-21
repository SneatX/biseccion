from sympy import sympify
from modules.biseccion import metodoBiseccion
from modules.limpiarConsola import limpiarPantalla

try:
    limpiarPantalla()
    print("""
    ╔═══════════════════════════╗
    ║    METODO DE BISECCION    ║
    ╚═══════════════════════════╝
    """)
    funcion = input("Ingrese la funcion a evaluar: f(x) = ")
    try:
        expr = sympify(funcion)
    except:
        raise ValueError("La función ingresada no es válida")

    intA = float(input("Ingrese el menor intervalo: "))
    intB = float(input("Ingrese el mayor intervalo: "))

    # Validar que el intervalo tenga un cambio de signo
    if expr.subs('x', intA) * expr.subs('x', intB) >= 0:
        raise ValueError("El intervalo dado no cumple con el teorema del bolzano")

    tolerancia = float(input("Ingrese la tolerancia: "))

    if tolerancia <= 0:
        raise ValueError("La tolerancia debe ser un número positivo")

    metodoBiseccion(funcion, intA, intB, tolerancia)

except ValueError as ve:
    print("Error:", ve)

except Exception as e:
    print("Ocurrió un error inesperado:", e)
