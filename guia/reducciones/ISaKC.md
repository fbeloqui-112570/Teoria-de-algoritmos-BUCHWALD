(★★) Definir los problemas de decisión de Independent Set y K-Clique. Hacer una reducción de Independet Set a K-Clique. Dada esta reducción, ¿podemos afirmar que K-Clique es un problema NP-Completo?

El problema de decision de Independent set es: Existen al menos k vertices tal que ninguno de ellos compartan aristas entre si.
El problema de decision de K-Clique es: Existen al menos k vertices tal que formen un subgrafo completo, es decir que desde cada uno de ellos pueda ir a todos los demas.

## Reduccion propuesta

Para reducir Independent Set a K clique, suponiendo que mi independent set es parte de un grafo G, basta con crearme un grafo G' que sea el grafo complemento de este ultimo.

# Existe Independent Set de al menos k vertices <-> Existe K clique de al menos k vertices

## Existe Independent Set de al menos k vertices -> Existe K clique de al menos k vertices

Si en mi grafo G tengo un Independent Set de al menos k vertices, eso quiere decir que tengo al menos k vertices de los cuales ninguno comparte aristas entre si, por lo que en G', esos vertices ahora van a estar todos conectados con todos los que antes no estaban conectados, es decir, voy a tener un clique de al menos k vertices.

## Existe Independent Set de al menos k vertices <- Existe K clique de al menos k vertices

Analogamente, si en G' tengo un subgrafo completo de al menos k vertices, es decir, un clique, eso quiere decir que desde cualquiera de esos k vertices puedo llegar a todos los demas que formen parte de ese clique, por lo que cada uno va a tener al menos k-1 adyacentes. Por lo que en mi grafo original, al no existir esas adyacencias, voy a tener k vertices que no van a estar conectados entre si, siendo asi un independent set de al menos k vertices.

## Conclusiones finales

Como Independent Set es NP-Completo, y logre reducir Independent Set a K-Clique, eso quiere decir que K-Clique es NP-Completo.
