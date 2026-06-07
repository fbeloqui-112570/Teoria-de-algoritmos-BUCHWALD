"""Alan y Bárbara están conviviendo en conjunto con n − 2 amigos (es decir, son n personas conviviendo). Deben organizar quién
cocinará cada una de las próximas n cenas (una persona debe cocinar sí o sí cada día, obviamente no tiene que ser siempre la misma).
Hay que considerar que cada persona desea cocinar a lo sumo 2 noches de estas n, y que cada uno de ellos tiene planes que pueden
hacer que algunas noches no puedan encargarse de la cena. Contando con la información de quién puede cada noche, ¿es posible
asignar un encargado/a de la cocina para cada una de las noches, sin que nadie cocine más de 2 de estas? ¿Cómo? Implementar
un algoritmo que, utilizando redes de flujo resuelva el problema (determine si se puede hacer una asignación, y si es así que nos
indique tal asignación). Indicar y justificar la complejidad del algoritmo implementado en las variables del problema."""

from grafo import Grafo
from ford_fulkerson import flujo


def cenas_amigos(disponibilidad):
    grafo = Grafo(es_dirigido=True)
    s = "superfuente"
    t = "supersumidero"
    amigos = set()
    grafo.agregar_vertice(s)
    grafo.agregar_vertice(t)
    for noche, disponibles in disponibilidad.items():
        grafo.agregar_vertice(noche)
        grafo.agregar_arista(noche, t, 1)
        for persona in disponibles:
            if persona not in amigos:
                amigos.add(persona)
                grafo.agregar_vertice(persona)
                grafo.agregar_arista(s, persona, 2)
                grafo.agregar_arista(persona, noche, 1)
    ff = flujo(s, t, grafo)
    res = []
    for (v, w), f in ff.items():
        if v != s and w != t:
            if f == 1:
                res.append((v, w))
    if len(res) == len(disponibilidad):
        return res, True
    return [], False
