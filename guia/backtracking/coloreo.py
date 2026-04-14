from grafo import *
def es_valido(grafo, actual, colores):
    for w in grafo.adyacentes(actual):
        if w in colores and colores[w] == colores[actual]:
            return False
    return True


def dfs(grafo, indice, vertices, colores, n):
    if indice == len(vertices):
        return True
    actual = vertices[indice]
    for color in range(n):
        colores[actual] = color
        if es_valido(grafo, actual, colores):
            if dfs(grafo, indice + 1, vertices, colores, n):
                return True
    del(colores[actual])
    return False

def coloreo(grafo: Grafo, n):
    colores = {}
    vertices = grafo.obtener_vertices()
    return dfs(grafo, 0, vertices, colores, n)

