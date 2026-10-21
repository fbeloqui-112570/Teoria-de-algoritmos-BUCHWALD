def caja_fuerte(k, s):
    return caja_fuerte_rec(k, s, 1, [], [])


def caja_fuerte_rec(k, s, indice, solucion_parcial, solucion_optima):
    if len(solucion_parcial) == k:
        if sum(solucion_parcial) == s:
            solucion_optima.append(solucion_parcial[:])
        return solucion_optima
    if indice == 10:
        return solucion_optima
    if sum(solucion_parcial) > s:
        return solucion_optima
    solucion_parcial.append(indice)
    solucion_optima = caja_fuerte_rec(
        k, s, indice + 1, solucion_parcial, solucion_optima
    )
    solucion_parcial.pop()
    return caja_fuerte_rec(k, s, indice + 1, solucion_parcial, solucion_optima)
