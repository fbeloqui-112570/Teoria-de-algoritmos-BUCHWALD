"""Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L
y un entero n devuelva todos los subconjuntos de L que suman exactamente n."""


def sumatorias_n(lista, n):
    solucion_parcial = []
    solucion_optima = []
    return sumatorias_n_rec(lista, n, 0, solucion_parcial, solucion_optima)


def sumatorias_n_rec(lista, n, indice, solucion_parcial, solucion_optima):
    if sum(solucion_parcial) == n:
        solucion_optima.append(solucion_parcial[:])
        return solucion_optima
    if indice == len(lista):
        return solucion_optima
    restantes = lista[indice:]
    if sum(solucion_parcial) + sum(restantes) < n:
        return solucion_optima
    actual = lista[indice]
    solucion_parcial.append(actual)
    if sum(solucion_parcial) <= n:
        solucion_optima = sumatorias_n_rec(
            lista, n, indice + 1, solucion_parcial, solucion_optima
        )
    solucion_parcial.pop()
    return sumatorias_n_rec(lista, n, indice + 1, solucion_parcial, solucion_optima)


if __name__ == "__main__":
    print(sumatorias_n([3, 4, 5, 1, 7], 9))
