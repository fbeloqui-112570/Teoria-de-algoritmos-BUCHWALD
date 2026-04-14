"""Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L
y un entero n devuelva todos los subconjuntos de L que suman exactamente n."""


def sumatorias_n(lista, n):
    soluciones = []
    sumatorias_n_rec(lista, n, 0, (0, []), soluciones)
    return soluciones


def sumatorias_n_rec(lista, n, indice, subconjunto, soluciones):
    suma_subconjunto, elem_subconjunto = subconjunto
    if suma_subconjunto == n:
        soluciones.append(elem_subconjunto[:])
        return None
    if suma_subconjunto > n or indice >= len(lista):
        return None
    elem_actual = lista[indice]
    suma_subconjunto += elem_actual
    elem_subconjunto.append(elem_actual)
    sumatorias_n_rec(
        lista, n, indice + 1, (suma_subconjunto, elem_subconjunto), soluciones
    )
    suma_subconjunto -= elem_actual
    elem_subconjunto.pop()
    sumatorias_n_rec(
        lista, n, indice + 1, (suma_subconjunto, elem_subconjunto), soluciones
    )
