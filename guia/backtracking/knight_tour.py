from ...grafo import Grafo


def knight_tour(n):
    grafo = grafo_caballo(n)
    for v in grafo.obtener_vertices():
        camino = [v]
        if camino_hamiltoniano(grafo, v, camino):
            return True
    return False


def camino_hamiltoniano(grafo: Grafo, vertice_actual, camino):
    if len(camino) == len(grafo.obtener_vertices()):
        return True
    for w in grafo.adyacentes(vertice_actual):
        if w not in camino:
            camino.append(w)
            if camino_hamiltoniano(grafo, w, camino):
                return True
            camino.pop()
    return False


def grafo_caballo(n):
    grafo = Grafo(es_dirigido=True)
    movimientos = [
        (2, 1),
        (1, 2),
        (-2, 1),
        (-1, 2),
        (-2, -1),
        (-1, -2),
        (2, -1),
        (1, -2),
    ]
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))
    for v in grafo.obtener_vertices():
        i, j = v
        for x, y in movimientos:
            posicion_nueva_i = i + y
            posicion_nueva_j = j + x
            if 0 <= posicion_nueva_i < n and 0 <= posicion_nueva_j < n:
                grafo.agregar_arista(v, (posicion_nueva_i, posicion_nueva_j))
    return grafo


def main():
    pass


if __name__ == "__main__":
    main()
