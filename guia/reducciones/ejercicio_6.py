"""(★★) Definir el problema de decisión de las N-Reinas.
Usar que N-Reinas es un problema NP-Completo para demostrar que Demostrar que Independent Set es un problema NP-Completo.

El problema de decision de las n reinas es que para cada posicion del tablero en la cual hay una reina colocada,
me fijo si esta posicion es compatible en base a los movimientos que puede hacer otra reina. En el caso de que sea
posible conocar n reinas en el tablero de modo que ninguna sea capaz de comerse entre si, entonces la respuesta a mi
problema de decision es que SI, en cambio si no es posible lograr esto entonces NO.

Ahora para demostrar que el problema de independent set es NP-completo voy a plantear la reduccion del problema de las n reinas(el cual es NP-completo)
al problema de independent set, lo cual me alcanzaria para demostrar que independent set es NP-completo.

Para ello la idea es pensar el tablero como un grafo, y cada casillero de este como un vertice v, donde los adyacentes a este vertice serian todas las posiciones
a las que puede acceder la reina dede este vertice v. Procedo a demostrar la ida y la vuelta.

El tablero cuenta con n reinas colocadas <-> El grafo es un independent set de al menos n vertices

El tablero cuenta con n reinas colocadas -> El grafo es un independent set de al menos n vertices:

Al haber transformado el tablero a un grafo y las posicones a vertices con sus respectivas adyacencias, si queremos llegar a n reinas,
tendriamos que ver que haya al menos n vertices que no puedan llegar a ninguno de ellos mediante sus adyacentes, es decir un independent set.

El tablero cuenta con n reinas colocadas <- El grafo es un independent set de al menos n vertices:

Viendo como quedo mi grafo con respecto al tablero original, nos damos cuenta de que al llegar a una cantidad n de vertices, que formen parte del
independent set, es decir, que no sean adyacentes entre si, es analogo a decir que tenemos n reinas que no se pueden comer entre ellas, ya que no tienen
forma de lograr eso con un movimiento.

De esta forma, queda demostrado que se puede reducir el problema de n reinas, el cual es NP-completo a Independent Set, por ende, Independent Set es NP-Completo.
"""
