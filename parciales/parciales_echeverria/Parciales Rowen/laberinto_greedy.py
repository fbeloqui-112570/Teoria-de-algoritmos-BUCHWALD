def recorrer_manzanas(cuadricula):
    n = len(cuadricula)
    m = len(cuadricula[0])
    i = j = 0
    resultado = [cuadricula[i][j]]

    while i < n - 1 and j < m - 1:
        if cuadricula[i + 1][j] > cuadricula[i][j + 1]:
            i += 1
        else:
            j += 1
        resultado.append(cuadricula[i][j])

    while i < n - 1:
        i += 1
        resultado.append(cuadricula[i][j])

    while j < m - 1:
        j += 1
        resultado.append(cuadricula[i][j])

    return resultado


def K(i, j) -> int:
    return 0


"""Este algoritmo es un algoritmo greedy ya que tengo un optimo local que consiste en que en cada iteracion
decido cual es el camino que mas madera tiene para ese momento, lo cual me va a llevar a un optimo global
donde voy a tener la mayor cantidad de madera posible. Este algoritmo no es optimo ya que puede ocurrir que
decida que un camino (i+1) sea mejor que un camino (j+1), pero si hubiese elegido este ultimo podria pasar 
que haya encontrado un camino con mas madera que todos los anteriores y yo nunca lo hubiese visto, por lo 
tanto el algoritmo no es optimo. Por ultimo la complejidad del algoritmo es O(n + m), ya que depende de 
si termino recorriendo mas filas que columnas y nunca recorro la cuadricula completa"""
