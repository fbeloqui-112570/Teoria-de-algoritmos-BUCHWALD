"""Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer,
y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad
de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la
mesa si todos los integrantes de su grupo pueden sentarse.
Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor
cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos)."""


def max_grupos_bodegon(P, W):
    solucion = [0, []]
    b_c(P, W, 0, [0, []], solucion)
    return solucion[1]


def b_c(P, W, indice, solucion_parcial, solucion_actual):
    suma_parcial, elementos_parcial = solucion_parcial
    suma_actual = solucion_actual[0]

    if suma_parcial > W:
        return None

    if suma_parcial <= W and suma_parcial > suma_actual:
        solucion_actual[0] = suma_parcial
        solucion_actual[1] = elementos_parcial[:]

    if indice >= len(P):
        return None

    actual = P[indice]

    suma_parcial += actual
    elementos_parcial.append(actual)
    b_c(
        P,
        W,
        indice + 1,
        [suma_parcial, elementos_parcial],
        solucion_actual,
    )

    suma_parcial -= actual
    elementos_parcial.pop()

    b_c(
        P,
        W,
        indice + 1,
        [suma_parcial, elementos_parcial],
        solucion_actual,
    )
