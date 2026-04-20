def lunatico(ganancias):
    if not ganancias:
        return []
    if len(ganancias) == 1:
        return [0]
    ganancia1, posiciones1 = pd(ganancias[0:-1], segundo_subarreglo=False)
    ganancia2, posiciones2 = pd(ganancias[1:], segundo_subarreglo=True)

    if ganancia1 >= ganancia2:
        return posiciones1
    else:
        return posiciones2


def pd(ganancias, segundo_subarreglo):
    if not ganancias:
        return 0, []
    if len(ganancias) == 1:
        posicion = 1 if segundo_subarreglo else 0
        return ganancias[0], [posicion]

    memo = [0] * len(ganancias)
    memo[0] = ganancias[0]
    memo[1] = max(ganancias[0], ganancias[1])

    for i in range(2, len(ganancias)):
        memo[i] = max(memo[i - 1], memo[i - 2] + ganancias[i])

    posiciones = reconstruir_arreglo(memo, segundo_subarreglo)
    return memo[-1], posiciones


def reconstruir_arreglo(memo, segundo_subarreglo):
    reconstruccion = []
    i = len(memo) - 1

    while i > -1:
        if i == 0 or memo[i] != memo[i - 1]:
            if segundo_subarreglo:
                reconstruccion.append(i + 1)
            else:
                reconstruccion.append(i)
            i -= 2
        else:
            i -= 1

    reconstruccion.reverse()
    return reconstruccion


def main():
    lista = [1, 5, 2, 1, 6, 1, 2, 1]
    print(lunatico(lista))


if __name__ == "__main__":
    main()
