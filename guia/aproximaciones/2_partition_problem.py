"""(★★★) El 2-Partition Problem como problema de optimización se describe tal que: Dado un conjunto de nn números positivos T={T1,T2,…,Tn}T={T1​,T2​,…,Tn​}, se particionan los números en dos subconjuntos S1S1​ y S2S2​ (con intersección vacía y unión = T) de forma de minimizar la sumatoria de cualquiera de los subconjuntos (min⁡max⁡(S1,S2)minmax(S1​,S2​)).

Para este problema, podemos plantear el siguiente algoritmo aproximado: Inicializar la solución como dos subconjuntos vacíos recorriendo los elementos de TT, para cada elemento se lo coloca en el subconjunto con menor sumatoria hasta el momento.

Demostrar que el algoritmo propuesto es una 3223​-Aproximación."""

# [10, 20, 90, 100, 200], -> solucion Greedy: [10, 90, 200], [20, 100]
#
# [10, 20, 90, 100, 200] -> solucion Optima: [20, 90, 100], [10, 200]
#
# Demostracion: sum(T) // 2 <=  sum(max(S)) < sum(T)) -> Cota para el maximo
# en el mejor de los casos T* = sum(s1) + sum(s2) = T
#
# En el peor de los casos yo se que es imposible que el maximo de los 2 subconjuntos sea igual al conjunto T, ya que al
# repartirse de manera intercalada, como mucho ambos suman lo mismo, o en el peor de los casos, uno termina teniendo mas de
# la mitad de la suma, por eso es una 3/2 aproximacion. Para el caso de arriba, T = 420 y en mi solucion optima, mi min(max) = 210,
# sin embargo en mi solucion greedy mi min(max) es 300 y en el otro 120, al ser mi T*=210, 210 * 1.5 = 315, lo cual esta muy cerca de mi
# 300 de la solucion greedy, es por esto que podemos confirmar que es una 3/2 aproximacion.
