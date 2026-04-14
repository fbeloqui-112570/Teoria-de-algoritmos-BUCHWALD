from grafo import Grafo


def subconjunto_no_adyacentes(grafo: Grafo, n):
    subconjunto = set()
    visitados = set()
    v = grafo.vertice_aleatorio()
    return subconjunto_no_adyacentes_dfs(grafo, n, v, subconjunto, visitados)


def subconjunto_no_adyacentes_dfs(grafo, n, v, subconjunto, visitados):
    if len(subconjunto) == n:
        return True
    if len(visitados) == len(grafo.obtener_vertices()):
        return False
    visitados.add(v)
    for vertice in grafo.obtener_vertices():
        if vertice not in grafo.adyacentes[v]:
            subconjunto.add(v)
