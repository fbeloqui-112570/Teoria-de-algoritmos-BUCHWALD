from grafo import Grafo


def independent_set(grafo):
    if not grafo.obtener_vertices():
        return []
    if len(grafo.obtener_vertices()) == 1:
        return [0]
    vertices = grafo.obtener_vertices()
    OPT = [0] * len(vertices)
    OPT[0] = vertices[0]
    OPT[1] = max(vertices[0], vertices[1])
    for i in range(2, len(vertices)):
        OPT[i] = max(OPT[i - 1], vertices[i] + OPT[i - 2])
    return reconstruccion(vertices, OPT)


def reconstruccion(vertices, OPT):
    i = len(vertices) - 1
    solucion = []
    while i >= 0:
        if i == 0:
            solucion.append(i)
            break
        if OPT[i - 1] != OPT[i]:
            solucion.append(i)
            i -= 2
        else:
            i -= 1
    solucion.reverse()
    return solucion


if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_vertice(100)
    grafo.agregar_vertice(20)
    grafo.agregar_vertice(30)
    grafo.agregar_vertice(70)
    grafo.agregar_vertice(50)
    vertices = grafo.obtener_vertices()
    for i in range(len(vertices) - 1):
        grafo.agregar_arista(vertices[i], vertices[i + 1])
    print(independent_set(grafo))
