"""
(★★) Dado un grafo en forma de grilla como el dado a continuación, donde cada vértice tiene un peso w(v)w(v),
se desea maximizar la sumatoria de los pesos de un Independent Set sobre dicho grafo.
"""


# a. Dar un algoritmo greedy que sirva de aproximación para la solución al problema.
def max_peso_independent_set(grafo):
    vertices_ordenados = sorted(grafo.obtener_vertices(), reverse=True)
    independent_set = set()
    for v in vertices_ordenados:
        mayor_local = True
        for w in grafo.adyacentes(v):
            if w in independent_set:
                mayor_local = False
                break
        if mayor_local:
            independent_set.add(v)
    return independent_set


# b. Demostrar que cualquier vértice es parte de la solución aproximada, o bien tiene peso menor (o igual) a alguno de sus adyacentes,
#  que es en efecto parte de dicha solución.
# Al haber ordenado mis vertices de menor a mayor, si yo estoy viendo un vertice mi decision es agregarlo o no, en el caso de agregarlo,
# una vez que yo vea sus adyacentes, el hecho de que no lo haya agregado quiere decir que uno de sus adyacentes ya es parte del independent set.
# Como este vertice ya era parte del independent set quiere decir que ya lo habia visto antes, y como estan ordenados de mayor a menos quiere decir
# que este vertice era al menos del mismo peso que el que estoy viendo ahora, por lo tanto queda demostrado que cualquier vertice es parte de la solucion
# o al menos uno de sus 4 adyacentes lo es.

# C. Para analizar que tan buena es la aproximacion, es necesario primero asumir un peor caso, suponiendo que mis vertices tienen peso [1, 2, 1, 1, 1]
# y son todos adyacentes con el 2, al ordenarlos de mayor a menor, estos quedarian de la forma [2, 1, 1, 1, 1]. Como primero voy a ver al 2, y voy a ver que
# este es mayor a cualquiera de los demas vertices adyacentes, lo voy a agregar a mi independent set y en consecuencia, no voy a agregar a ninguno de los adyacentes,
# de esta forma me estaria perdiendo de mi solucion optima la cual seria [1, 1, 1, 1] (peso = 4 vs peso = 2). Es por esto que en el peor de los casos, yo estaria agregando
# a mi solucion a un vertice cuando me convenia agregar a mis otros 4 adyacentes, siendo de esta forma mi solucion 1/4 de lo que seria mi solucion optima, lo que la convierte
# en una 4 aproximacion.
