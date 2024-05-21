import matplotlib.pyplot as plt
import numpy as np
from modules.limpiarConsola import limpiarPantalla

def metodoBiseccion(funcion, a, b, tolera):
    fx = lambda x: eval(funcion)

    tramo = b - a
    iteraciones = 0

    a_vals = [a]
    b_vals = [b]
    c_vals = []

    while tramo >= tolera and a != b:
        c = (a + b) / 2
        fa = fx(a)
        fb = fx(b)
        fc = fx(c)
        
        if fc == 0:  # Si fc es exactamente 0, c es la raíz exacta
            a = b = c
            break

        if fa * fc < 0:
            b = c
        elif fb * fc < 0:
            a = c
        
        tramo = b - a
        iteraciones += 1
        
        # Guardar los valores para la gráfica
        a_vals.append(a)
        b_vals.append(b)
        c_vals.append(c)


    print('Raíz en: ', c)
    print('Error en tramo: ', tramo)
    print('Iteraciones: ', iteraciones)

    x = np.linspace(a_vals[0], b_vals[0], 400)
    y = fx(x)

    plt.plot(x, y, label='f(x)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.axvline(c, color='r', linestyle='--', label='Raíz aproximada')

    for i in range(len(c_vals)):
        plt.plot([a_vals[i], b_vals[i]], [0, 0], 'bo-')
        plt.plot(c_vals[i], 0, 'ro')

    plt.title('Método de Bisección')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()
