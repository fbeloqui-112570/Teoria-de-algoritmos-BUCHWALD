# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
from grafo import Grafo


def submarinos(matriz):
    solucion_parcial = []
    submarinos, grafo = crear_grafo(matriz)
    vertices = grafo.obtener_vertices()
    peor_caso = vertices[:]
    return submarinos_rec(
        grafo, set(), submarinos, vertices, 0, solucion_parcial, peor_caso
    )


def submarinos_rec(
    grafo,
    submarinos_iluminados,
    submarinos,
    vertices,
    indice,
    solucion_parcial,
    solucion_optima,
):
    if len(submarinos_iluminados) == len(submarinos):
        if len(solucion_parcial) < len(solucion_optima):
            return solucion_parcial[:]
        return solucion_optima
    if indice == len(vertices):
        return solucion_optima
    actual = vertices[indice]
    nuevos_descubiertos = calcular_submarinos_radio(
        grafo, actual, submarinos_iluminados, submarinos
    )
    if len(nuevos_descubiertos) > len(submarinos_iluminados) and len(
        solucion_parcial
    ) + 1 < len(solucion_optima):
        solucion_parcial.append(actual)
        solucion_optima = submarinos_rec(
            grafo,
            nuevos_descubiertos,
            submarinos,
            vertices,
            indice + 1,
            solucion_parcial,
            solucion_optima,
        )
        solucion_parcial.pop()
    return submarinos_rec(
        grafo,
        submarinos_iluminados,
        submarinos,
        vertices,
        indice + 1,
        solucion_parcial,
        solucion_optima,
    )


def calcular_submarinos_radio(grafo, vertice, submarinos_iluminados, set_submarinos):
    nuevos = submarinos_iluminados.copy()
    if vertice in set_submarinos:
        nuevos.add(vertice)
    for w in grafo.adyacentes(vertice):
        if w in set_submarinos:
            nuevos.add(w)
    return nuevos


def crear_grafo(matriz):
    grafo = Grafo(es_dirigido=True)
    submarinos = set()
    radio = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (2, 0),
        (2, 1),
        (2, 2),
        (1, 2),
        (0, 2),
        (-1, 2),
        (-2, 2),
        (-2, 1),
        (-2, 0),
        (-2, -1),
        (-2, -2),
        (-1, -2),
        (0, -2),
        (1, -2),
        (2, -2),
        (2, -1),
    ]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]:
                submarinos.add((i, j))
            grafo.agregar_vertice((i, j))
    for v in grafo.obtener_vertices():
        i, j = v
        for fila, columna in radio:
            adyacente_i = i + fila
            adyacente_j = j + columna
            if 0 <= adyacente_i < len(matriz) and 0 <= adyacente_j < len(matriz[0]):
                grafo.agregar_arista(v, (adyacente_i, adyacente_j))
    return submarinos, grafo
