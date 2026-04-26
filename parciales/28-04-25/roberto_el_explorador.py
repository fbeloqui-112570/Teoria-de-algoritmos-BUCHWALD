def roberto(provisiones, distancias, prov_iniciales, k_consumo):
    contador = 0
    for i in range(len(distancias)):
        prov_iniciales -= k_consumo * distancias[i]
        if prov_iniciales < 0:
            prov_iniciales += provisiones[i - 1]
            contador += 1
    return contador


"""COMPLEJIDAD: La complejidad del algoritmo en cuestion es O(d) siendo en este caso D la cantidad de distancias que hay.
Ya que solo se recorren una unica vez y el resto de operaciones son O(1).
JUSTIFICACION GREEDY: Es un algoritmo Greedy ya que su regla es que en cada iteracion se fija en llegar lo mas lejos posible antes de quedarse sin proviciones,
al hacer esto tengo un optimo local en el cual solo me detengo una vez que me quede sin provisiones lo cual me va a dar una sucesion de 
optimos locales donde se minimiza la cantidad de paradas que se hicieron."""


if __name__ == "__main__":
    print(roberto([10, 5, 2], [6, 5, 4, 2], 7, 1))
