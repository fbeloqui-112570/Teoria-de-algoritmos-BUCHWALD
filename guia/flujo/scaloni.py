"""Para poder cortar con el juego del rival, Scaloni cuenta con información precisa minuto a minuto. En un momento dado, tiene la
información perfecta de qué jugador puede darle un pase a cuál otro (independientemente de quién tenga la pelota) o marcar un gol.
Scaloni quiere saber a qué jugador, o jugadores, es indispensable marcar para evitar que nos marquen un gol. Suponiendo que una
jugada arranca en el arquero contrario, y que se tiene la información de qué jugador de ese equipo puede pasarle la pelota a cuál/es
otro/s (incluyendo al arquero), considerando que esto no es necesariamente recíproco (no todos los jugadores pueden hacer los mismos
pases o goles, ¿o vos podés dar los mismos pases que Messi?), y cuáles jugadores podrían marcar un gol en ese momento, indicar
cuáles son los mínimos jugadores contrarios a marcar de tal forma que no sea posible que nos marquen un gol (no podemos marcar
al arquero). Resolver este problema utilizando redes de flujo. Pueden suponer que la función flujo(red, s, t) les devuelve
tanto la asignación de flujo a cada arista, como también la Red Residual resultante de aplicar el algoritmo de Ford-Fulkerson. Indicar
y justificar la complejidad del algoritmo planteado. Para todo el problema, considerar que, si bien hay un único arquero, podrían
haber n jugadores de campo (simplemente para no quedarse con que son 10 nada más)."""

from grafo import Grafo
from ford_fulkerson import flujo


def marcas(
    informacion: Grafo,
):  # informacion es de tipo grafo, donde los vertices son los jugadores y sus adyacentes son a quienes le pueden pasar la pelota
    grafo = Grafo(es_dirigido=True)
    s = "arquero_rival"
    t = "arquero_equipo"
    for v in informacion.obtener_vertices():
        if v == s or v == t:
            continue
        v_in = (v, "in")
        v_out = (v, "out")
        grafo.agregar_vertice(v_in)
        grafo.agregar_vertice(v_out)
        grafo.agregar_arista(v_in, v_out, 1)
        for w in informacion.adyacentes(v):
            w_in = (w, "in")
            grafo.agregar_arista(v_out, w_in, int(float("inf")))
    grafo.agregar_vertice(s)
    grafo.agregar_vertice(t)
    for w in informacion.adyacentes(s):
        grafo.agregar_arista(s, w, int(float("inf")))
    for v in informacion.obtener_vertices():
        if t in informacion.adyacentes(v):
            grafo.agregar_arista(v, t, int(float("inf")))
    res = []
    ff = flujo(s, t, grafo)
    for (v, w), f in ff.items():
        if w == t and f == 1:
            res.append(v)
    return res
