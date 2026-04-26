def scheduling(charlas):
    solucion_mejor = []
    scheduling_bt(charlas, 0, [], solucion_mejor)
    return solucion_mejor


def scheduling_bt(charlas, indice, solucion_parcial, solucion_mejor):
    if len(solucion_parcial) > len(solucion_mejor):
        solucion_mejor.clear()
        solucion_mejor.extend(solucion_parcial)

    if indice == len(charlas):
        return None

    charla_actual = charlas[indice]

    if es_valido(charla_actual, solucion_parcial):
        solucion_parcial.append(charla_actual)
        scheduling_bt(charlas, indice + 1, solucion_parcial, solucion_mejor)
        solucion_parcial.pop()  # Backtrack (deshacemos el cambio)

    scheduling_bt(charlas, indice + 1, solucion_parcial, solucion_mejor)


def es_valido(charla, solucion_parcial):
    start2, end2 = charla
    for start1, end1 in solucion_parcial:
        if max(start1, start2) < min(end1, end2):
            return False
    return True
