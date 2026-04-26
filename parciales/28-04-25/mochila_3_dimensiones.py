"""Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso
(para ella) que pueda y que entre en su mochila. Tiene 2 limitaciones. La primera: no puede guardar más peso que lo que permita su
mochila (tiene límite hasta W). La segunda: como sabe que puede entrar en un estado de locura e inconciencia temporal, se puso
un límite que no comprará por más de P precio en total (es decir, la suma de todo lo comprado). Cada producto tiene 3 valores
asociados: su valor (vi

, que Laura definió en base a su subjetividad), su precio (pi) y su peso (wi).

Implementar un algoritmo que, utilizando programación dinámica, permita determinar qué productos debe comprar Laura tal
que no superen el peso máximo que puede llevar y el precio máximo dispuesto a pagar, y que logre maximizar el valor obtenido
(dados por la suma de los elementos comprados). También escribir el algoritmo que permita reconstruir la solución.
Indicar y justificar la complejidad del algoritmo implementado."""


def mochila(productos, W, P):
    if not productos:
        return []
    matriz = []
    for _ in range(len(productos) + 1):
        fila = []
        for _ in range(W + 1):
            columna = []
            for _ in range(P + 1):
                columna.append(0)
            fila.append(columna)
        matriz.append(fila)
    for i in range(1, len(matriz)):
        for j in range(1, len(matriz[0])):
            for k in range(1, len(matriz[0][0])):
                p_i, w_i, v_i = productos[i - 1]
                if w_i <= j and p_i <= k:
                    matriz[i][j][k] = max(
                        matriz[i - 1][j][k],
                        matriz[i - 1][j - w_i][k - p_i] + v_i,
                    )
                else:
                    matriz[i][j][k] = matriz[i - 1][j][k]
    return reconstruccion(productos, matriz)


def reconstruccion(productos, matriz):
    i = len(matriz) - 1
    j = len(matriz[0]) - 1
    k = len(matriz[0][0]) - 1
    lista = []
    while i > 0:
        if matriz[i][j][k] == matriz[i - 1][j][k]:
            i -= 1
            continue
        p_i, w_i, _ = productos[i - 1]
        lista.append(productos[i - 1])
        i -= 1
        j -= w_i
        k -= p_i
    lista.reverse()
    return lista
