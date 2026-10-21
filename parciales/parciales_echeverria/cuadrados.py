"""
El teorema de los cuadrados de Lagrange especifica que cualquier número entero no
negativo n puede expresarse como la suma de cuatro cuadrados de enteros no negativos: n
= w2 + x
2 + y
2 + z
2
. Implementar un algoritmo de backtracking que, dado el valor de n,

indique cuales son los cuadrados que lo componen. ¿Cuál es su complejidad?
Ejemplos:
● 42 = 4
2 + 4
2 + 3
2 + 1
2

● 310 = 17
2 + 4
2 + 2
2 + 1
"""
def cuadrados(n):
    return cuadrados_rec(n, 0, [], [])

def sumar_cuadrados(cuadrados):
    resultado = 0
    for cuadrado in cuadrados:
        resultado += cuadrado * cuadrado
    return resultado


def cuadrados_rec(n, indice, solucion_parcial, solucion_total):
    if len(solucion_parcial) == 4:
        if sumar_cuadrados(solucion_parcial) == n:
            return solucion_parcial[:]
        return solucion_total
    if sumar_cuadrados(solucion_parcial) > n or indice * indice > n:
        return solucion_total
    solucion_parcial.append(indice)
    solucion_total = cuadrados_rec(n, indice, solucion_parcial, solucion_total)
    solucion_parcial.pop()
    return cuadrados_rec(n, indice + 1, solucion_parcial, solucion_total)


print(cuadrados(310))
