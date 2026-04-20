def bodegon_dinamico(P, W):
    if len(P) == 0:
        return []
    if len(P) == 1 and P[0] <= W:
        return P
    matriz = []
    for i in range(len(P) + 1):
        fila = []
        for j in range(W + 1):
            fila.append(0)
        matriz.append(fila)
    for i in range(1, len(P) + 1):
        for j in range(1, W + 1):
            if P[i - 1] <= j:
                matriz[i][j] = max(
                    matriz[i - 1][j], matriz[i - 1][j - P[i - 1]] + P[i - 1]
                )
            else:
                matriz[i][j] = matriz[i - 1][j]
    return matriz


def reconstruir_matriz(P, matriz):
    lista = []
    i = len(matriz) - 1
    j = len(matriz[0]) - 1
    while i > 0:
        if matriz[i][j] == 0:
            break
        if matriz[i][j] == matriz[i - 1][j]:
            i -= 1
            continue
        lista.append(P[i - 1])
        j -= P[i - 1]
        i -= 1
    lista.reverse()
    return lista


def main():
    P = [3, 4, 9, 2, 5]
    W = 15
    matriz = bodegon_dinamico(P, W)
    print(reconstruir_matriz(P, matriz))


if __name__ == "__main__":
    main()
