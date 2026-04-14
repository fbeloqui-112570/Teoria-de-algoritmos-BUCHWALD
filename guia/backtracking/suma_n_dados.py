def sumatoria_dados(n, s):
    soluciones = []
    suma_dados(s, n, 0, [], soluciones)
    return soluciones


def suma_dados(suma, cant_faltan, suma_actual, elementos, soluciones):
    if cant_faltan == 0:
        if suma_actual == suma:
            soluciones.append(list(elementos))
        return soluciones

    if suma_actual > suma:
        return soluciones
    if suma_actual + 1 * cant_faltan > suma or suma_actual + 6 * cant_faltan < suma:
        return soluciones

    for valor in range(1, 6 + 1):
        elementos.append(valor)
        suma_dados(suma, cant_faltan - 1, suma_actual + valor, elementos, soluciones)
        elementos.pop()

    return soluciones
