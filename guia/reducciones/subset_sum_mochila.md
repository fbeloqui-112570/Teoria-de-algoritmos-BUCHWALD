
(★★) Definir los problemas de decisión de Subset Sum y Problema de la Mochila. Sabiendo que Subset Sum es NP-Completo, demostrar que el Problema de la Mochila es NP-Completo.

Problema de decision de Subset Sum: Existen al menos una combinacion de elementos de un conjunto que sumen W.

Problema de decision de la mochila: Existe una combinacion de elementos que sumen al menos V y que pesen a lo sumo W en total.

# Demostracion

## Validador

Para demostrar que el problema de la mochila es NP-Completo, primero tengo que demostrar que esta en NP. Para ello construyo el siguiente validador:

```python
def validador(mochila, elementos, V, W):
  for objeto in mochila:
    if objeto not in elementos:
      return False
  suma_pesos = 0
  suma_valores = 0
  for valor, peso in mochila:
    suma_pesos += peso
    suma_valores += valor 
  if suma_pesos > W or suma_valores < V:
    return False
  return True
```

La complejidad de este validador es O(m * e) siendo m la cantidad de elementos de la mochila y e la cantidad de elementos totales. Ya que recorro toda
la mochila y por cada elemento me fijo si esta existe en la lista de elementos o no. Por lo tanto al ser un validador polinomial, esta en NP.

## Reduccion Propuesta

Para reducir Subset Sum al problema de la mochila, se me ocurre hacer que V = W.

## Existen Solucion para Subset Sum <-> Existe solucion para el problema de la mochila

### Existen Solucion para Subset Sum -> Existe solucion para el problema de la mochila

Si tengo un subconjunto de elementos S dentro de mi conjunto original E el cual suma exactamente W, la suma de esos elementos no puede pasarse de W, este W es el mismo
W de la capacidad de la mochila y el valor de cada uno de estos elementos en en el conjunto S es un tanto el valor como el peso de estos elementos en la mochila.

### Existen Solucion para Subset Sum <- Existe solucion para el problema de la mochila

Al tener una mochila con capacidad W y una suma de elementos que da V, como V = W, eso quiere decir que la capacidad tiene que ser exactamente igual a la suma de los valores de los elementos, lo cual en definitiva es un subset sum.

# Conclusiones finales

Como logre reducir Subset Sum (el cual es un problema NP-Completo) al problema de la mochila, y tambien demostre que el problema de la mochila esta en NP, es que puedo decir que el problema de la mochila es NP-Completo
