def cobertura(casas, R, K):
    lista = []
    casas_ordenadas = sorted(casas)
    inicio = casas_ordenadas[0]
    antena = inicio
    for casa in casas_ordenadas:
        distancia = casa - inicio
        if distancia <= R:
            antena = casa
        else:
            diferencia = distancia - R
            antena = casa - diferencia
            lista.append(antena)
        if casa - antena > R:
            inicio = casa
    if antena not in lista:
        lista.append(inicio)
    return lista


if __name__ == "__main__":
    casas = [8.5, 1.0, 3.0, 7.0, 2.5]
    print(cobertura(casas, 2.0, 10.0))
