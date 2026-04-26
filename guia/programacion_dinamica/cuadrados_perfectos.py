"""Dado un número n, indicar la cantidad más económica (con menos términos) de escribirlo como suma de cuadrados perfectos, utilizando Programación Dinámica.
Indicar y justificar la complejidad del algoritmo implementado.

Aclaración: siempre es posible escribir a n como suma de n términos de 1^2, por lo que siempre existe solución.
Sin embargo, la expresión 10 = 3^2 + 1^2 es una manera más económica de escribirlo para n=10"""


def terminos(n):
    cuadrados_perf = [i**2 for i in range(n + 1) if 0 < i**2 <= n]
    OPT = [0] * (n + 1)
    for i in range(n + 1):
        minimo = i
        for cuadrado in cuadrados_perf:
            if cuadrado <= i:
                cant = 1 + OPT[i - cuadrado]
                if cant < minimo:
                    minimo = cant
        OPT[i] = minimo
    return OPT[n]


if __name__ == "__main__":
    print(terminos(10))
