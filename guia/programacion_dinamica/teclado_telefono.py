from ...grafo import Grafo


def numeros_posibles(k, n):
    if n == 0:
        return 0
    if n == 1:
        return k
    grafo = vecinos_teclas()
    cant = []
    for _ in range(n):
        cant_teclas = []
        for _ in range(10):
            cant_teclas.append(0)
        cant.append(cant_teclas)
    for tecla in range(10):
        cant[0][tecla] = 0
        cant[1][tecla] = 1
    for i in range(2, n + 1):
        for tecla in range(10):
            contador = 0
            for w in grafo.adyacentes(tecla):
                contador += cant[i - 1][w]
            cant[i][tecla] = contador
    return cant[n][k]


def vecinos_teclas():
    grafo = Grafo()
    for n in range(10):
        grafo.agregar_vertice(n)
    grafo.agregar_arista(0, 8)
    grafo.agregar_arista(1, 2)
    grafo.agregar_arista(1, 4)
    grafo.agregar_arista(2, 1)
    grafo.agregar_arista(2, 3)
    grafo.agregar_arista(2, 5)
    grafo.agregar_arista(3, 2)
    grafo.agregar_arista(3, 6)
    grafo.agregar_arista(4, 1)
    grafo.agregar_arista(4, 5)
    grafo.agregar_arista(4, 7)
    grafo.agregar_arista(5, 2)
    grafo.agregar_arista(5, 4)
    grafo.agregar_arista(5, 6)
    grafo.agregar_arista(5, 8)
    grafo.agregar_arista(6, 3)
    grafo.agregar_arista(6, 5)
    grafo.agregar_arista(6, 9)
    grafo.agregar_arista(7, 4)
    grafo.agregar_arista(7, 8)
    grafo.agregar_arista(8, 0)
    grafo.agregar_arista(8, 5)
    grafo.agregar_arista(8, 9)
    grafo.agregar_arista(8, 0)
    grafo.agregar_arista(9, 6)
    grafo.agregar_arista(9, 8)
    return grafo


def main():
    print(numeros_posibles(1, 2))


if __name__ == "__main__":
    main()
