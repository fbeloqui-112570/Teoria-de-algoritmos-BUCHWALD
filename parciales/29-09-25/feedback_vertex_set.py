"""El problema conocido como Feedback Vertex Set (FVS) indica: Dado un grafo (por simplificación, no dirigido), indicar vértices a
eliminar de dicho grafo de tal manera que el grafo quede acíclico.
En nuestro grafo cada vértice i tiene un valor positivo vi

. Implementar un algoritmo que, por backtracking, encuentre el mínimo
FVS (es decir, el conjunto de vértices que sea un FVS, y sea de suma mínima). Si bien es obvio, el grafo no cuenta con una primitiva
tiene_ciclos (e, incluso, si la tuviera, sería poco conveniente usarla, recomendamos pensar por qué)."""

from ...grafo import Grafo


def feedback_vertex_set(grafo: Grafo):
    vertices = grafo.obtener_vertices()
    solucion_parcial = []
    solucion_actual = [vertices]
    b_t(grafo, vertices, 0, solucion_parcial, solucion_actual)
    return solucion_actual[0]


def es_valido(grafo: Grafo, solucion_parcial):
    visitados = set()
    for v in grafo.obtener_vertices():
        if v in solucion_parcial:
            continue
        if v in visitados:
            return False
        visitados.add(v)
    return True


def b_t(grafo: Grafo, vertices, indice, solucion_parcial, solucion_actual):
    if sum(solucion_parcial) >= sum(solucion_actual[0]):
        return
    if indice == len(vertices):
        if es_valido(grafo, solucion_parcial):
            solucion_actual[0] = solucion_parcial[:]
            return
    actual = vertices[indice]
    solucion_parcial.append(actual)
    b_t(grafo, vertices, indice + 1, solucion_parcial, solucion_actual)
    solucion_parcial.pop()
    b_t(grafo, vertices, indice + 1, solucion_parcial, solucion_actual)
