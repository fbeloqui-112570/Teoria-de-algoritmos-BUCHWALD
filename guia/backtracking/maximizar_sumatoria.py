def max_sumatoria_n(lista, n):
    solucion_parcial = [0, []]
    solucion_optima = [0, []]
    suma, elementos = max_sumatoria_n_rec(
        lista, n, 0, solucion_parcial, solucion_optima
    )
    return elementos


def max_sumatoria_n_rec(lista, n, indice, solucion_parcial, solucion_optima):
    suma_parcial, elementos_parcial = solucion_parcial
    suma_optima, elementos_optima = solucion_optima
    if suma_parcial == n:
        return [suma_parcial, elementos_parcial[:]]
    if indice == len(lista):
        if suma_parcial > suma_optima:
            return [suma_parcial, elementos_parcial[:]]
        else:
            return solucion_optima
    actual = lista[indice]
    elementos_parcial.append(actual)
    suma_parcial += actual
    if suma_parcial <= n:
        suma_optima, elementos_optima = max_sumatoria_n_rec(
            lista,
            n,
            indice + 1,
            [suma_parcial, elementos_parcial],
            [suma_optima, elementos_optima],
        )
    elementos_parcial.pop()
    suma_parcial -= actual
    return max_sumatoria_n_rec(
        lista,
        n,
        indice + 1,
        [suma_parcial, elementos_parcial],
        [suma_optima, elementos_optima],
    )


if __name__ == "__main__":
    print(max_sumatoria_n([1, 3, 5, 2, 1], 7))
