"""Se tiene un sistema monetario (ejemplo, el nuestro).
Se quiere dar "cambio" de una determinada cantidad de plata.
Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes.
El algoritmo recibirá un arreglo de valores del sistema monetario,
y la cantidad de cambio objetivo a dar, y debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada.
Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar si es óptimo, o dar un contraejemplo.
¿Por qué se trata de un algoritmo Greedy? Justificar"""


def cambio(monedas, monto):
    lista = []
    contador = monto
    i = len(monedas) - 1
    while contador != 0:
        if monedas[i] <= contador:
            contador -= monedas[i]
            lista.append(monedas[i])
        else:
            i -= 1
    return lista


if __name__ == "__main__":
    print(cambio([1, 10, 25, 50, 100], 230))
