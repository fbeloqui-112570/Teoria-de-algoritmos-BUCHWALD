def mochila_pd(elementos, W):
    OPT = []
    for i in range(len(elementos) + 1):
        fila = []
        for j in range(W + 1):
            fila.append(0)
        OPT.append(fila)
    for i in range(1, len(elementos) + 1):
        for j in range(1, W + 1):
            peso, beneficio = elementos[i - 1]
            if peso <= j:
                OPT[i][j] = max(OPT[i - 1][j], OPT[i - 1][j - peso] + beneficio)
            else:
                OPT[i][j] = OPT[i - 1][j]
    return reconstruccion(elementos, OPT)


def reconstruccion(elementos, OPT):
    resultado = []
    i = len(OPT) - 1
    j = len(OPT[0]) - 1
    while i > 0:
        if OPT[i][j] == 0:
            break
        if OPT[i][j] == OPT[i - 1][j]:
            i -= 1
            continue
        peso, beneficio = elementos[i - 1]
        resultado.append((peso, beneficio))
        i -= 1
        j -= peso
    resultado.reverse()
    return resultado


if __name__ == "__main__":
    elementos = [(2, 3), (3, 4), (4, 5), (5, 6)]
    W = 5
    print(mochila_pd(elementos, W))
