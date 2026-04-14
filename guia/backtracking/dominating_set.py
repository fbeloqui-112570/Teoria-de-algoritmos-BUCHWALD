from ...grafo import Grafo


def dominating_set_min(grafo: Grafo):
    vertices = grafo.obtener_vertices()
    solucion_parcial = []
    solucion = [vertices]
    dominating_set_min_rec(grafo, vertices, 0, solucion_parcial, solucion)
    return solucion[0]


def es_dominating_set(grafo: Grafo, solucion_parcial):
    visitados = set()
    for vertice in solucion_parcial:
        visitados.add(vertice)
        for w in grafo.adyacentes(vertice):
            visitados.add(w)
    if len(visitados) == len(grafo.obtener_vertices()):
        return True
    return False


def dominating_set_min_rec(grafo: Grafo, vertices, indice, solucion_parcial, solucion):
    if len(solucion_parcial) >= len(solucion[0]):
        return
    if indice == len(vertices):
        if es_dominating_set(grafo, solucion_parcial):
            solucion[0] = solucion_parcial[:]
        return
    actual = vertices[indice]
    solucion_parcial.append(actual)
    dominating_set_min_rec(grafo, vertices, indice + 1, solucion_parcial, solucion)
    solucion_parcial.pop()
    dominating_set_min_rec(grafo, vertices, indice + 1, solucion_parcial, solucion)


def main():
    pass


if __name__ == "__main__":
    main()
