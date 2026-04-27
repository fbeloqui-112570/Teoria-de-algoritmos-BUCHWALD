"""Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer,
y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad
de personas que integran el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la
mesa si todos los integrantes de su grupo pueden sentarse.
Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor
cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos)."""


def max_grupos_bodegon(P, W):
    solucion_parcial = []
    solucion_optima = []
    return max_grupos_bodegon_rec(P, W, 0, solucion_parcial, solucion_optima)


def max_grupos_bodegon_rec(P, W, indice, solucion_parcial, solucion_optima):
    if indice == len(P):
        if len(solucion_parcial) > len(solucion_optima):
            return solucion_parcial[:]
        return solucion_optima
    if len(solucion_parcial) + (len(P) - indice) <= len(solucion_optima):
        return solucion_optima
    actual = P[indice]
    solucion_parcial.append(actual)
    if sum(solucion_parcial) <= W:
        solucion_optima = max_grupos_bodegon_rec(
            P, W, indice + 1, solucion_parcial, solucion_optima
        )
    solucion_parcial.pop()
    return max_grupos_bodegon_rec(P, W, indice + 1, solucion_parcial, solucion_optima)
