"""Tenemos un grafo no dirigido que representa una grilla de n × n. Definimos que un vértice en la fila i y columna j es el vértice (i, j).
Todos los vértices tienen exactamente 4 adyacentes, salvo los de los bordes, es decir los de la primera y última fila o columna.
Implementar una función que dado el grafo y m puntos iniciales distintos en la grilla (i1, j1), · · · ,(im, jm), determine si existen m
caminos disjuntos (de vértices) donde cada uno comience en un punto inicial, y termine en m puntos diferentes del borde. En los
ejemplos del dorso, el de la izquierda tiene solución (la cuál se muestra) mientras que el de la derecha no tiene solución. Utilizar
redes de flujo para resolver este problema. Indicar y justificar la complejidad del algoritmo implementado."""

from grafo import Grafo
from ford_fulkerson import flujo


def caminos_disjuntos_vertices(grafo: Grafo, puntos_iniciales):
    red = Grafo(es_dirigido=True)

    s = "SUPER_FUENTE"
    t = "SUPER_SUMIDERO"
    red.agregar_vertice(s)
    red.agregar_vertice(t)

    for v in grafo.obtener_vertices():
        v_in = (v, "in")
        v_out = (v, "out")
        red.agregar_vertice(v_in)
        red.agregar_vertice(v_out)

        red.agregar_arista(v_in, v_out, 1)

        if v in puntos_iniciales:
            red.agregar_arista(s, v_in, int(float("inf")))

        if len(grafo.adyacentes(v)) < 4:
            red.agregar_arista(v_out, t, int(float("inf")))

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            v_out = (v, "out")
            w_in = (w, "in")

            red.agregar_arista(v_out, w_in, int(float("inf")))

    flujo_maximo = flujo(red, s, t)

    m = len(puntos_iniciales)
    contador = 0
    for (v, w), f in flujo_maximo.items():
        if v == s:
            contador += f
    return contador == m
