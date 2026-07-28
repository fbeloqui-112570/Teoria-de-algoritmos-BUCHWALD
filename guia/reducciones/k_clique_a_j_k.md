El problema del Subgrafo K-J Completo (SKJC) se define como: Dado un grafo y dos valores K y J, ¿existe un subgrafo dentro de
dicho grafo, de a lo sumo K vértices donde todos los vértices se conecten con al menos J de los demás vértices del subgrafo?
Demostrar que el problema del Subgrafo K-J Completo es un problema NP-Completo. Recomendamos recordar que el problema de
K-Clique es un problema NP-Completo. Leer atentamente en la definición del problema los “a lo sumo” y “al menos”.

# Validador

Para demostrar que el problema del Subgrafo K-J Completo esta en NP, primero hay que escribir un validador polinomial:

```python
def validador(grafo, subgrafo, k, j):
  set_grafo = set(grafo.obtener_vertices())
  for v in subgrafo:
    if v not in set_grafo:
      return False
  if len(subgrafo) > k:
    return False
  set_subgrafo = set(subgrafo.obtener_vertices())
  for v in subgrafo:
    contador = 0
    for w in subgrafo.adyacentes(v):
      if w in set_subgrafo:
        contador += 1
    if contador < j:
      return False
  return True
```

La complejidad de este algoritmo es de O(K + E), siendo E las aristas del subgrafo, que puede ser una cantidad mayor a J pero nunca
mayor a K en el peor de los casos, por lo tanto este validador es polinomial y demostramos que el problema esta en NP.

# Reduccion Propuesta

Ahora para demostrar que este problema es NP-Completo. Vamos a utilizar otro problema que es NP-Completo. En este caso vamos a utilizar
K-Clique.

La reduccion propuesta consiste en utilizar el mismo grafo con k'= k, el cual representa la cantidad de vertices que forman parte del
subgrafo, y j = k-1, que representa la cantidad minima de vertices adyacentes a un vertice que forma parte del SKJC que tambien son parte
del SKJC.

Decimos entonces que:

## Existe Clique de al menos k vertices <-> Existe SKJC

### Existe Clique de al menos k vertices -> Existe SKJC

Para demostrar la ida podemos ver que en mi grafo copia, al ser mi k' = k, significa que voy a tener k vertices que forman parte del
subgrafo, y como j = k-1, al ser un subgrafo completo, significa que voy a poder ir a todos los demas vertices que formen parte de ese
subgrafo, que por definicion al ser completo, siempre va a ser al menos k-1 la cantidad de adyacentes de cada vertice del subgrafo.

### Existe SKJC -> Existe Clique de al menos k vertices

Para demostrar la vuelta, vemos que mi k = k' por lo que en este caso mi clique va a contar con la misma cantidad de vertices que la
del subgrafo SKJC, y como este subgrafo es completo, signfica que voy a poder ir a todos los vertices que formen del subgrafo, lo cual
es igual a k-1 que a su vez es igual a j. Demostrando asi que si tengo un SKJC en el grafo copia, tengo un K-Clique en el grafo original.

# Conclusion

Como pudimos reducir el problema de K-Clique, el cual es NP-Completo, a SKJC, el cual previamente demostramos que esta en NP, es que
podemos decir que el SKJC, es un problema NP-Completo.
