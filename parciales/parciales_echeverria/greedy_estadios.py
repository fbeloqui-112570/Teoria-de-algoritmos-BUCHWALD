def recorridos(grafo, vertice_inicial):
    vertices = grafo.obtener_vertices()
    recorrido = [vertice_inicial]
    visitados = {vertice_inicial}
    actual = vertice_inicial

    while len(visitados) < len(vertices):
        distancia_minima = float("inf")
        siguiente = None

        for w in grafo.adyacentes(actual):
            if w not in visitados:
                distancia = grafo.peso_arista(actual, w)

                if distancia < distancia_minima:
                    distancia_minima = distancia
                    siguiente = w

        visitados.add(siguiente)
        recorrido.append(siguiente)
        actual = siguiente

    recorrido.append(vertice_inicial)
    return recorrido

