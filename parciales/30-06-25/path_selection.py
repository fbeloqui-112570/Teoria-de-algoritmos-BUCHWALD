def path_selection(grafo, caminos):
    solucion_parcial = []
    solucion_optima = []
    vertices = grafo.obtener_vertices()
    return path_selection_rec(
        grafo, caminos, vertices, 0, solucion_parcial, solucion_optima
    )


def path_selection_rec(
    grafo, caminos, vertices, indice, solucion_parcial, solucion_optima
):
    if indice == len(vertices):
        if len(solucion_parcial) > len(solucion_optima):
            return solucion_parcial[:]
        return solucion_optima
    restantes = len(vertices) - len(solucion_parcial)
    if len(solucion_parcial) + restantes < len(solucion_optima):
        return solucion_optima
    actual = vertices[indice]
    solucion_parcial.append(actual)
    if es_valido(caminos, actual):
        solucion_optima = path_selection_rec(
            grafo, caminos, vertices, indice + 1, solucion_parcial, solucion_optima
        )
    solucion_parcial.pop()
    return path_selection_rec(
        grafo, caminos, vertices, indice + 1, solucion_parcial, solucion_optima
    )


def es_valido(caminos, actual):
    contador = 0
    for camino in caminos:
        if actual in camino:
            contador += 1
    return contador == 1
