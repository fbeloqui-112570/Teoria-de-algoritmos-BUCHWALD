from grafo import Grafo


def nreinas(n):
    grafo = crear_grafo(n)
    vertices = grafo.obtener_vertices()
    lista = []
    resultado = n_reinas_rec(grafo, vertices, 0, lista, n)
    if resultado is not None:
        return resultado
    return []


def n_reinas_rec(grafo: Grafo, vertices, indice, lista, n):
    if len(lista) == n:
        return lista[:]
    if indice == len(vertices):
        return None
    actual = vertices[indice]
    if es_valido(grafo, actual, lista):
        lista.append(actual)
        if n_reinas_rec(grafo, vertices, indice + 1, lista, n) is not None:
            return lista
        lista.pop()
    return n_reinas_rec(grafo, vertices, indice + 1, lista, n)


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
