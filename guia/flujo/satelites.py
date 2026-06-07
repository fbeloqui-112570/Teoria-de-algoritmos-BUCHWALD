"""(★★★) Una red de satélites se construyó para permitir la comunicación entre una nave espacial y la tierra.
Ciertos Satélites pueden intercambiar mensajes entre otros (ida y vuelta). Algunos con la tierra, otros con la nave espacial.
Contamos con la red y se pide medir su robustez: ¿cuántos satélites (en el peor de los casos) se pueden romper que dejen
incomunicada la nave con la tierra? ¿Cuáles? Utilizando redes de flujo, resolver el problema.
Indicar y justificar la complejidad del algoritmo implementado. Recordar que esto último debe estar en las variables del problema."""

from grafo import Grafo
from cola import Cola
from ford_fulkerson import flujo


def construir_red(satelites, conexiones):
    # conexiones es una lista de tuplas (satelite1, satelite2), donde cada satélite
    # puede ser también la tierra o la nave
    red = Grafo(es_dirigido=True)
    red.agregar_vertice("tierra")
    red.agregar_vertice("nave")
    for satelite in satelites:
        red.agregar_vertice(satelite + "in")
        red.agregar_vertice(satelite + "out")
        red.agregar_arista(satelite + "in", satelites + "out", 1)
    for s1, s2 in conexiones:
        if s1 == "nave":
            red.agregar_arista(s1, s2 + "in", int(float("inf")))
        elif s2 == "tierra":
            red.agregar_arista(s1 + "out", "tierra", int(float("inf")))
        else:
            red.agregar_arista(s1 + "out", s2 + "in", int(float("inf")))
    return red


def eliminar_satelites(satelites, conexiones):
    red = construir_red(satelites, conexiones)
    _, red_residual = flujo(red, "tierra", "nave")
    alcanzables = encontrar_alcanzables(red_residual, satelites)
    return calcular_corte_vertices(alcanzables, satelites)


def encontrar_alcanzables(red_residual):
    alcanzables = set()
    cola = Cola()

    cola.encolar("tierra")
    alcanzables.add("tierra")

    while not cola.esta_vacia():
        actual = cola.desencolar()

        for ady in red_residual.adyacentes(actual):
            if ady not in alcanzables and red_residual.peso(actual, ady) > 0:
                alcanzables.add(ady)
                cola.encolar(ady)

    return alcanzables


# Corte de vértices


def calcular_corte_vertices(alcanzables, satelites):
    corte = []

    for satelite in satelites:
        if satelite + "in" in alcanzables and satelite + "out" not in alcanzables:
            corte.append(satelite)

    return corte
