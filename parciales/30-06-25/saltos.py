"""Dado un arreglo de números positivos, donde cada elemento representa el máximo número de pasos que podemos dar desde esa
posición, implementar un algoritmo que, utilizando programación dinámica determine la menor cantidad de saltos a realizar
para llegar al final del arreglo (comenzamos en la posición 0). También escribir el algoritmo que permita reconstruir la solución.
Indicar y justificar la complejidad del algoritmo implementado.
Por ejemplo, si el arreglo es [2, 3, 1, 1, 4], la solución óptima es ir desde la posición 0 a la posición 1 (saltando 1 lugar,
teniendo máximo 2 desde el inicio), y de allí a la posición 4 (saltando 3 lugares, que es el máximo desde dicha posición), logrando
llegar al final en 2 saltos."""


def saltos(arreglo):
    if not arreglo:
        return []
    if len(arreglo) == 1:
        return [0]
    OPT = [0] * len(arreglo)
    OPT[1] = 1
    j = 0

    for i in range(1, len(arreglo)):
        while j < i and arreglo[j] + j < i:
            j += 1

        OPT[i] = 1 + OPT[j]
    return OPT


if __name__ == "__main__":
    print(saltos([2, 3, 1, 1, 4]))
