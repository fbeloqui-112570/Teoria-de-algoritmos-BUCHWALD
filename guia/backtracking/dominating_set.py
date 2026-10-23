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
    return len(visitados) == len(grafo.obtener_vertices())


def dominating_set_min_rec(
    grafo: Grafo, vertices, indice, solucion_parcial, solucion_optima
):
    if len(solucion_parcial) >= len(solucion_optima):
        return solucion_optima
    if indice == len(vertices):
        if es_dominating_set(grafo, solucion_parcial):
            return solucion_parcial[:]
        return solucion_optima
    actual = vertices[indice]
    solucion_parcial.append(actual)
    solucion_optima = dominating_set_min_rec(
        grafo, vertices, indice + 1, solucion_parcial, solucion_optima
    )
    solucion_parcial.pop()
    solucion_optima = dominating_set_min_rec(
        grafo, vertices, indice + 1, solucion_parcial, solucion_optima
    )
    return solucion_optima


def main():
    pass


if __name__ == "__main__":
    main()
