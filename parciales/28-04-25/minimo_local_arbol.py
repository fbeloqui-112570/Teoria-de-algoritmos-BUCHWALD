def minimo_local_arbol(arbol):
    if not arbol.izq and not arbol.der:
        return arbol

    val_izq = arbol.izq.valor if arbol.izq else float("inf")
    val_der = arbol.der.valor if arbol.der else float("inf")

    if arbol.valor < val_izq and arbol.valor < val_der:
        return arbol

    if val_izq < val_der:
        return minimo_local_arbol(arbol.izq)
    else:
        return minimo_local_arbol(arbol.der)


# Complejidad: T(n) = T(n/2) + n^0 -> A = 1, B = 2, C = 0
# log en base 2 de 1 = 0 = C -> n^0 * log n = O(log n)
