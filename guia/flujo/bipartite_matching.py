"""(★★) Dado un grafo bipartito no dirigido, un match es un subconjunto de las aristas en el cual para todo
vértice vv a lo sumo una arista del match incide en vv (en el match, tienen grado a lo sumo 1).
Decimos que el vértice vv está matcheado si hay alguna arista que incida en él (sino, está unmatcheado).
El matching máximo es aquel en el que tenemos la mayor cantidad de aristas (matcheamos la mayor cantidad posible).
Dar una metodología para encontrar el matching máximo de un grafo, explicando en detalle cómo se modela el problema,
cómo se lo resuelve y cómo se consigue el matching máximo. ¿Cuál es el orden temporal de la solución implementada?"""

from grafo import Grafo
from ford_fulkerson import flujo


def bipartite_matching(grafo: Grafo, colores):
    nuevo_grafo = Grafo(es_dirigido=True, vertices_init=grafo.obtener_vertices())
    s = "superfuente"
    t = "supersumidero"
    nuevo_grafo.agregar_vertice(s)
    nuevo_grafo.agregar_vertice(t)
    for v, color in colores.items():
        if v in nuevo_grafo.obtener_vertices():
            continue
        nuevo_grafo.agregar_vertice(v)
        if color == 0:
            nuevo_grafo.agregar_arista(s, v, 1)
        elif color == 1:
            nuevo_grafo.agregar_arista(v, t, 1)
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if grafo.estan_unidos(v, s) and grafo.estan_unidos(w, t):
                nuevo_grafo.agregar_arista(v, w, 1)
    ff = flujo(s, t, nuevo_grafo)
    res = []
    for (v, w), f in ff.items():
        if nuevo_grafo.estan_unidos(s, v) and nuevo_grafo.estan_unidos(w, t) and f == 1:
            res.append((v, w))
    return res, len(res)
