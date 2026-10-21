from grafo import Grafo
from cola import Cola


def construir_red(satelites, conexiones):
    # conexiones es una lista de tuplas (satelite1, satelite2), donde cada satélite
    # puede ser también la tierra o la nave
    red = Grafo(dirigido=True)
    red.agregar_vertice("tierra")
    red.agregar_vertice("nave")
    for satelite in satelites:
        red.agregar_vertice(satelite + "in")
        red.agregar_vertice(satelite + "out")
        red.agregar_arista(satelite + "in", satelitee + "out", 1)
    for s1, s2 in conexiones:
        if s1 == "nave":
            red.agregar_arista(s1, s2 + "in", float("inf"))
        elif s2 == "tierra":
            red.agregar_arista(s1 + "out", "tierra", float("inf"))
        else:
            red.agregar_arista(s1 + "out", s2 + "in", float("inf"))
    return red


def eliminar_satelites(satelites, conexiones):
    red = construir_red(satelites, conexiones)
    _, red_residual = flujo_max(red, "tierra", "nave")
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


# Corte mínimo


def encontrar_corte_minimo(grafo_original, red_residual):
    alcanzables = encontrar_alcanzables(red_residual)

    corte = []

    for v in alcanzables:
        for w in grafo_original.adyacentes(v):
            if w not in alcanzables:
                corte.append((v, w))

    return corte


# Carlos DISJOINT PATH ARISTAS


def crear_red(calles, casa, escuela):
    red = Grafo(es_dirigido=True)
    for esquina in calles:
        red.agregar_vertice(esquina)
    visitados = set()
    ficticios = {}
    for esquina in calles:
        for conectada in calles.adyacentes(esquina):
            if conectada in visitados:
                continue
            elif esquina == casa or conectada == escuela:
                red.arista(esquina, conectada, peso=1)
            elif esquina == escuela or conectada == casa:
                red.arista(conectada, esquina, peso=1)
            else:
                red.agregar_vertice(esquina + conectada)
                red.arista(esquina, conectada, peso=1)
                red.arista(conectada, esquina + conectada, peso=1)
                red.arista(esquina + conectada, esquina, peso=1)
                ficticios[esquina + conectada] = (esquina, conectada)
        visitados.add(esquina)
        return red, ficticios


def carlos(calles, cant_hijos, casa, escuela):
    red, ficticios = crear_red(calles, casa, escuela)
    flujo = flujo_maximo(red)
    cantCaminos = 0
    for conectada in red.adyacentes(casa):
        if flujo[casa][conectada] > 0:
            cantCaminos += 1
    if cantCaminos < cant_hijos:
        return None

    # corregimos los flujos para que se cancelen si van ida y vuelta:
    for ficticio in ficticios:
        v, w = ficticios[ficticio]
        if flujo[v][w] == 1 and flujo[ficticio][v] == 1:
            flujo[v][w] = 0
            flujo[w][ficticio] = 0
            flujo[ficticio][v] = 0

    caminos = []
    for i in range(cant_hijos):
        camino = []
        camino.append(casa)
        v = casa
        while v != escuela:
            for w in red.adyacentes(v):
                if flujo[v][w] == 1:
                    flujo[v][w] = 0
                    v = w
                    if v not in ficticios:
                        camino.append(v)
                    break
        caminos.append(camino)
    return caminos


# Disjoint paths


def construir_caminos(grafo, flujos_aristas, s, t):
    res = []

    while True:
        camino = [s]
        actual = s
        while actual != t:
            for w in grafo.adyacentes(actual):
                if flujos_aristas[(actual, w)] == 0:
                    continue
                flujos_aristas[(actual, w)] = 0
                actual = w
                camino.append(w)
                break
            if camino == [s]:
                return res
        res.append(camino)


# Disjoint paths vértices


def construir_caminos_v(grafo_transformado, flujo, s, t):
    caminos = []

    while True:
        actual = s
        camino = [s]

        while actual != {t}:
            encontrado = False

            for w in grafo_transformado.adyacentes(actual):
                if flujo.get((actual, w), 0) == 0:
                    continue

                flujo[(actual, w)] = 0
                actual = w
                encontrado = True

                if actual.endswith("_in"):
                    v = actual[:-3]

                    if v != str(s) and v != str(t):
                        camino.append(v)

                break

            if not encontrado:
                return caminos

        camino.append(t)
        caminos.append(camino)


def devolver_favores(grafo, valores):
    red = armar_red_favores(grafo, valores)
    flujo = flujo_max(red)

    for vertice in grafo:
        if grafo.estan_unidos(vertice, "sumidero"):
            if flujo[(vertice, "sumidero")] < valores[vertice]:
                return False

    return True


def armar_red_favores(grafo, valores):
    red = grafo.copy()

    red.agregar_vertice("fuente")
    red.agregar_vertice("sumidero")

    for vertice, valor in valores.items():
        if valor * -1 > 0:
            red.agregar_arista(vertice, "sumidero", valor)
        elif valor * -1 < 0:
            red.agregar_arista("fuente", vertice, -valor)


def organizar_cenas(
    n, disponibilidad
):  # Disponibilidad es un diccionario {día_cena: [personas que pueden]}
    red = armar_red_cenas(n, disponibilidad)
    flujo = flujo_maximo(red)

    for i in range(n):
        if flujo[(f"cena{i}", "sumidero")] == 0:
            return False

    return True


def armar_red_cenas(n, disponibilidad):
    red = Grafo()
    red.agregar_vertice("fuente")
    red.agregar_vertice("sumidero")
    for i in range(n):
        red.agregar_vertice(f"persona{i}")
        red.agregar_vertice(f"cena{i}")
        red.agregar_arista("fuente", f"persona{i}", 2)
        red.agregar_arista(f"cena{i}", "sumidero", 1)
    for dia, personas in disponibilidad:
        for persona in personas:
            red.agregar_arista(persona, dia, 1)

    return red
