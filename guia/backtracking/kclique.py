# Implementar un algoritmo que, dado un grafo no dirigido, obtenga el clique de mayor tamaño dentro del mismo (utilizando
# backtracking).


def clique(grafo):
    return clique_rec(grafo, grafo.obtener_vertices(), 0, [], [])


def es_clique(grafo, solucion_parcial, v):
    for w in solucion_parcial:
        if not grafo.hay_arista(v, w):
            return False
    return True


def clique_rec(grafo, vertices, indice, solucion_parcial, solucion_optima):
    if indice == len(vertices):
        if len(solucion_parcial) > len(solucion_optima):
            return solucion_parcial[:]
        return solucion_optima
    actual = vertices[indice]
    if es_clique(grafo, solucion_parcial, actual):
        solucion_parcial.append(actual)
        solucion_optima = clique_rec(
            grafo, vertices, indice + 1, solucion_parcial, solucion_optima
        )
        solucion_parcial.pop()
    return clique_rec(grafo, vertices, indice + 1, solucion_parcial, solucion_optima)
