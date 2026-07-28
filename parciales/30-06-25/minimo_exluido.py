"""Implementar una función que, dado un arreglo ordenado y sin repetidos de valores enteros no negativos, obtenga el mínimo
valor que no se encuentre en el arreglo. Indicar y justificar adecuadamente la complejidad del algoritmo.
Por ejemplo:
minimoExcluido([0, 1, 5]) --> 2
minimoExcluido([1, 3, 5]) --> 0
minimoExcluido([0, 1, 2, 3, 4, 5]) --> 6
minimoExcluido([0, 1, 2, 3, 4, 5, 1234567]) --> 6"""


def minimo_exluido(arr):
    return minimo_exluido_rec(0, len(arr) - 1, arr)


def minimo_exluido_rec(inicio, fin, arr):
    if inicio > fin:
        return inicio
    mitad = (inicio + fin) // 2
    if mitad != arr[mitad]:
        return minimo_exluido_rec(inicio, mitad, arr)
    return minimo_exluido_rec(mitad + 1, fin, arr)


if __name__ == "__main__":
    print(minimo_exluido([0, 1, 2, 3, 4, 5]))
