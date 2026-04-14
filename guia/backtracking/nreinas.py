def calcular_siguiente_pos(pos, n):
    i, j = pos
    if j == n - 1:
        return i + 1, 0
    else:
        return i, j + 1


def es_compatible(reinas_colocadas, n, pos):
    fila, columna = pos
    for i in range(n):
        if (i, columna) in reinas_colocadas:
            return False
    for j in range(n):
        if (fila, j) in reinas_colocadas:
            return False
    for i in range(n):
        for j in range(n):
            if i - j == fila - columna:
                if (i, j) in reinas_colocadas:
                    return False
            if i + j == fila + columna:
                if (i, j) in reinas_colocadas:
                    return False
    return True


def n_reinas_rec(tablero, n, pos, reinas_colocadas):
    if len(reinas_colocadas) == n:
        return True

    i, j = pos
    if i == n:
        return False

    siguiente = calcular_siguiente_pos(pos, n)

    if es_compatible(reinas_colocadas, n, pos):
        reinas_colocadas.append((i, j))
        if n_reinas_rec(tablero, n, siguiente, reinas_colocadas):
            return True
        reinas_colocadas.pop()

    if n_reinas_rec(tablero, n, siguiente, reinas_colocadas):
        return True

    return False


def nreinas(n):
    tablero = crear_tablero(n)
    reinas_colocadas = []
    if n_reinas_rec(tablero, n, (0, 0), reinas_colocadas):
        return reinas_colocadas
    return None


def crear_tablero(n):
    tablero = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(',')
        tablero.append(fila)
    return tablero


def main():
    resultado = nreinas(4)
    if resultado:
        for fila in resultado:
            print(fila)
    else:
        print("No hay solución")


if __name__ == '__main__':
    main()
