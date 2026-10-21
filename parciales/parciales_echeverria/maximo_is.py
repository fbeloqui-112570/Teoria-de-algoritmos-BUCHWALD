def independent_set(grafo):
    vertices = grafo.obtener_vertices()
    return independent_set_rec(grafo, vertices, 0, [], [])

def es_independent_set(grafo, solucion, v):
    for vertice in solucion:
        if v in grafo.adyacentes(vertice):
            return False
    return True



def independent_set_rec(grafo, vertices, indice, solucion_parcial, solucion_total):
    if indice == len(vertices):
        if len(solucion_parcial) > len(solucion_total):
            return solucion_parcial[:]
        return solucion_total
    v = vertices[indice]
    if es_independent_set(grafo, solucion_parcial, v):
        solucion_parcial.append(v)
        solucion_total = independent_set_rec(grafo, vertices, indice + 1, solucion_parcial, solucion_total)
        solucion_parcial.pop()
    return independent_set_rec(grafo, vertices, indice + 1, solucion_parcial, solucion_total)
