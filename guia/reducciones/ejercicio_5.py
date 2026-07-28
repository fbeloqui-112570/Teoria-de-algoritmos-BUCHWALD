"""
(★) Para cada uno de los siguientes problemas, implementar un verificador polinomial y justificar su complejidad.

a. Dado un número por parámetro, si es la solución al problema de búsqueda del máximo en un arreglo.

b. Dado un arreglo, si es la solución a tener el arreglo ordenado.

c. Dadas un arreglo de posiciones de reinas, si es la solución de colocar al menos N-reinas en un tablero NxN.
"""


def verificar_maximo(numero, arr):
    if numero not in arr:
        return False
    if len(arr) == 1 and arr[0] == numero:
        return True
    maximo = arr[0]
    for elemento in arr:
        maximo = max(maximo, elemento)
    return numero == maximo


def verificar_arreglo_ordenado(arr):
    arr_ordenado = sorted(arr)
    return arr == arr_ordenado


def verificar_tablero_n_reinas(tablero, n):
    contador = 0
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == 1:
                contador += 1
                for fila in range(n):
                    if fila == i:
                        continue
                    if tablero[fila][j] == 1:
                        return False
                for columna in range(n):
                    if columna == j:
                        continue
                    if tablero[i][columna] == 1:
                        return False
                for fila in range(n):
                    for columna in range(n):
                        if fila == i and columna == j:
                            continue
                        if fila + columna == i + j or columna - fila == j - i:
                            if tablero[fila][columna] == 1:
                                return False
    if contador != n:
        return False
