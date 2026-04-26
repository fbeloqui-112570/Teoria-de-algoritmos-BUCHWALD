"""Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica,
permita cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo.
El algoritmo debe devolver el valor del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como se muestra
en el ejemplo con n = 10. Indicar y justificar la complejidad del algoritmo."""


def problema_soga(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    OPT = [0] * (n + 1)
    OPT[1] = 1
    OPT[2] = 2
    OPT[3] = 3
    for i in range(4, n + 1):
        maximo = 0
        for j in range(0, i + 1):
            if OPT[j] * OPT[i - j] > maximo:
                maximo = OPT[j] * OPT[i - j]
        OPT[i] = maximo
    return OPT[n]


if __name__ == "__main__":
    print(problema_soga(7))
