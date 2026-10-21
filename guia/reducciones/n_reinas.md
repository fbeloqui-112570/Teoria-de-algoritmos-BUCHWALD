(★★) Definir el problema de decisión de las N-Reinas. Usar que N-Reinas es un problema NP-Completo para demostrar que Independent Set es un problema NP-Completo.

# Problema de decision
El problema de decision de n reinas se define como: Existen al menos n reinas las cuales puedo colocar en un tablero de ajedrez para que no puedan comerse entre si.

Sabiendo que N-Reinas es NP-Completo, para demostrar que Independent Set es NP-Completo vamos a reducir N-Reinas a Independent Set.

# Reduccion Propuesta

Para lograr la reduccion, me creo un grafo G' en el cual cada uno de los vertices va a representar una posicion en el tablero y las aristas representan si desde ese vertice puedo llegar a otro con alguno de los movimientos de la reina.

# Existen al menos n reinas que no pueden comerse entre si <-> Existe independent set de al menos k vertices.


## Existen al menos n reinas que no pueden comerse entre si -> Existe independent set de al menos k vertices.

Si tenemos un tablero con n reinas distribuidas de tal forma que ninguna pueda comerse a otra, en G' vamos a tener k vertices que no estan unidos con ningun de esos otros k-1 vertices, siendo asi un independent set de tamaño k.

## Existen al menos n reinas que no pueden comerse entre si <- Existe independent set de al menos k vertices.

Si en G' tengo un independent set de al menos k vertices, si cada vertice equivale a una posicion en el tablero, entonces aquellos k vertices que no estan unidos con los demas k-1 vertices del independent set representan cada una de las posiciones desde las cuales una reina no puede llegar a comerse a otra.

# Conclusiones finales

Por lo tanto, como pude reducir el problema de N reinas a independent set, queda demostrado que Independent set es NP-Completo.
