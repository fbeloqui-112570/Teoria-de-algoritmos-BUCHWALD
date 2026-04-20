def laberinto(matriz):
    if not matriz:
        return 0
    MEMO = []
    n = len(matriz)
    m = len(matriz[0])
    for _ in range(len(matriz)):
        fila = []
        for _ in range(len(matriz[0])):
            fila.append(0)
        MEMO.append(fila)

    MEMO[0][0] = matriz[0][0]

    for fila in range(1, n):
        MEMO[fila][0] = MEMO[fila - 1][0] + matriz[fila][0]
    for columna in range(1, m):
        MEMO[0][columna] = MEMO[0][columna - 1] + matriz[0][columna]

    for fila in range(1, n):
        for columna in range(1, m):
            MEMO[fila][columna] = (
                max(MEMO[fila - 1][columna], MEMO[fila][columna - 1])
                + matriz[fila][columna]
            )
    return MEMO[-1][-1]


def main():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(laberinto(matriz))


if __name__ == "__main__":
    main()
