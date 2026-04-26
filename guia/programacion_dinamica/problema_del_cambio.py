"""Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.
Se desea devolver el cambio pedido, usando la mínima cantidad de monedas/billetes.
Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores del sistema monetario,
y la cantidad de cambio objetivo a dar, y devuelva qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizda.
Indicar y justificar la complejidad del algoritmo implementado."""
# [1, 5, 6, 9] monto = 11


def cambio(monedas, monto):
    if monto == 0:
        return [0], []
    OPT = [0] * (monto + 1)
    usadas = [0] * (monto + 1)
    for i in range(1, monto + 1):
        minimo = i
        usada = 1
        for moneda in monedas:
            if moneda <= i:
                cantidad = 1 + OPT[i - moneda]
                if cantidad < minimo:
                    minimo = cantidad
                    usada = moneda
        OPT[i] = minimo
        usadas[i] = usada
    return reconstruccion(monto, usadas)


def reconstruccion(monto, usadas):
    lista = []
    i = monto
    while i > 0:
        lista.append(usadas[i])
        i -= usadas[i]
    return lista


if __name__ == "__main__":
    print(cambio([1, 5, 6, 9], 11))
