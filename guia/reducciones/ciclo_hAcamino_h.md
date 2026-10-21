(★★★) Definir los problemas de decisión de Camino Hamiltoniano y Ciclo Hamiltoniano. Sabiendo que Ciclo Hamiltoniano es NP-Completo, demostrar que Camino Hamiltoniano es NP-Completo.

El problema de decision de Camino Hamiltoniano es: Existe un camino que permita recorrer todos los vertices de un grafo sin repetir vertices.

El problema de decision de Ciclo Hamiltoniano es: Existe un ciclo dentro de un grafo que permita recorrer todos sus vertices y volver al vertice de inicio sin repetir ninguno.

# Demostracion

Primero tengo que demostrar que Camino Hamiltoniano esta en NP. Para eso propongo el siguiente validador

## Validador

```python
def validador(grafo, vertices: set, camino: list):
    if len(vertices) !== len(camino):
        return False
    i = 0
    visitados = {}
    for i in range(len(camino)):
        v = camino[i]
        if v not in grafo.obtener_vertices():
            return False
        if v in visitados:
            return False
        visitados.add(v)
        if i == 0:
            continue
        if v not in grafo.adyacentes(camino[i-1]):
            return False
    return True
```
La complejidad de este validador es de O(V + E), ya que se recorren todos los vertices del grafo una unica vez para chequear si el camino es correcto y si se repiten vertices, utilizando un set para que las verificaciones sean en O(1) y ademas se recorren todas las aristas de cada vertice.

## Reduccion Propuesta

Para reducir ciclo hamiltoniano a camino hamiltoniano, se me ocurre crearme un grafo G' el cual va a ser una copia de G con la diferencia de que el vertice inicial ahora va a estar separado en 2 vertices, un vertice de entrada al cual van a tener todas las aristas que le llegaban en el grafo original, llamado v'' y un vertice de salida el cual va a contener a todas las aristas de las cuales salia en el grafo original, llamado v' ambos desconectados entre si.

## Existe Ciclo Hamiltoniano en G <-> Existe Camino Hamiltoniano en G'

### Existe Ciclo Hamiltoniano en G -> Existe Camino Hamiltoniano en G'

Si yo tengo un ciclo hamiltoniano en G, eso quiere decir que mi vertice final e inicial es el mismo, si en G' tengo un camino hamiltoniano, eso significa que los vertices que las aristas que antes salian de v ahora forman parte de v', mientras que aquellas que entraban a v ahora forman parte de v'', dandome asi un camino Hamiltoniano.

### Existe Ciclo Hamiltoniano en G <- Existe Camino Hamiltoniano en G'

Al tener un camino hamiltoniano en G', al unir v' y v'' en un mismo vertice voy a tener tanto las entradas de v'' como las salidad de v' en un mismo vertice lo cual me genera un ciclo, dandome asi un ciclo hamiltoniano en el grafo original.

# Conclusiones finales

Al haber demostrado que el Camino Hamiltoniano esta en NP y que pude reducir el Ciclo Hamiltoniano el cual es un problema NP-Completo al Camino Hamiltoniano, queda demostrado que Camino Hamiltoniano es NP-Completo.
