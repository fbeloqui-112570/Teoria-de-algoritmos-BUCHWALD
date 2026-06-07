from grafo import Grafo
from collections import deque


def flujo(grafo, s, t):
    asignacion = {}
    for v in grafo:
        for w in grafo.adyacentes(v):
            asignacion[(v, w)] = 0
    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, s, t)
    while camino is not None:
        capacidad_residual_camino = min_peso(grafo_residual, camino)
        for i in range(1, len(camino)):
            if grafo.estan_unidos(camino[i - 1], camino[i]):
                asignacion[(camino[i - 1], camino[i])] += capacidad_residual_camino
            else:
                asignacion[(camino[i], camino[i - 1])] -= capacidad_residual_camino
            actualizar_grafo_residual(
                grafo_residual, camino[i - 1], camino[i], capacidad_residual_camino
            )
        camino = obtener_camino(grafo_residual, s, t)

    return asignacion


def actualizar_grafo_residual(grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso_arista(u, v)
    if peso_anterior == valor:
        grafo_residual.borrar_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
    if not grafo_residual.estan_unidos(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
        grafo_residual.cambiar_peso(v, u, grafo_residual.peso_arista(v, u) + valor)


def copiar(g):
    nuevo = Grafo(True, g.obtener_vertices())
    for v in g:
        for w in g.adyacentes(v):
            nuevo.agregar_arista(v, w, g.peso_arista(v, w))
    return nuevo


def obtener_camino(g, org, dst):
    padre = {org: None}
    cola = deque()
    cola.append(org)
    while len(cola) > 0:
        v = cola.popleft()
        if v == dst:
            camino = []
            while v is not None:
                camino.append(v)
                v = padre[v]
            return camino[::-1]
        for w in g.adyacentes(v):
            if w not in padre:
                padre[w] = v
                cola.append(w)
    return None


def min_peso(grafo, camino):
    cap = grafo.peso_arista(camino[0], camino[1])
    for i in range(1, len(camino) - 1):
        cap = min(cap, grafo.peso_arista(camino[i], camino[i + 1]))
    return cap
