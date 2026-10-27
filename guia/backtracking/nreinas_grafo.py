from grafo import Grafo


def nreinas(n):
    grafo = crear_grafo(n)
    vertices = grafo.obtener_vertices()
    resultado = n_reinas_rec(grafo, vertices, 0, [], [], n)
    if resultado is not None:
        return resultado
    return []


def n_reinas_rec(grafo: Grafo, vertices, indice, solucion_parcial, solucion_optima, n):
    if len(solucion_parcial) == n:
        return solucion_parcial[:]
    if indice == len(vertices):
        return solucion_optima
    actual = vertices[indice]
    if es_valido(grafo, actual, solucion_parcial):
        solucion_parcial.append(actual)
        solucion_optima = n_reinas_rec(grafo, vertices, indice + 1, solucion_parcial, solucion_optima, n)
        solucion_parcial.pop()
    return n_reinas_rec(grafo, vertices, indice + 1, solucion_parcial, solucion_optima, n)


def es_valido(grafo: Grafo, actual, lista):
    for elemento in lista:
        if actual in grafo.adyacentes(elemento):
            return False
    return True


def crear_grafo(n):
    grafo = Grafo()
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))
    for v in grafo.obtener_vertices():
        fila, columna = v
        for i in range(fila, n):
            if i != fila:
                grafo.agregar_arista(v, (i, columna))
        for j in range(columna, n):
            if j != columna:
                grafo.agregar_arista(v, (fila, j))
        for i in range(n):
            for j in range(n):
                if i != fila and j != columna:
                    if i + j == fila + columna or j - i == columna - fila:
                        grafo.agregar_arista(v, (i, j))
    return grafo


def main():
    print(nreinas(4))


if __name__ == "__main__":
    main()
