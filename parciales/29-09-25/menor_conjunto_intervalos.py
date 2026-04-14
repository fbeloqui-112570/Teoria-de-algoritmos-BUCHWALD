"""Implementar un algoritmo greedy que dada una lista de intervalos de formato [a, b] (con a <= b) determine el menor conjunto
de intervalos que incluyan el mismo rango que los intervalos originales. Indicar y justificar la complejidad del algoritmo. Justificar
por qué es un algoritmo Greedy. ¿El algoritmo da siempre la solución óptima? Si lo hace, justificar, si no dar un contraejemplo.
Ejemplos:
[1, 3], [5, 7], [2, 4] → [1, 4], [5, 7]
[3, 5], [1, 2], [2, 3], [7, 10], [5, 7] → [1, 10]
[5, 8], [3, 7], [4, 5], [10, 15], [9, 13], [11, 14] → [3, 8], [9, 15]
[1.3, 2.8], [2.97, 3.2], [0, 1.5], [2.95, 3] → [0, 2.8], [2.95, 3.2]
Notar que, por ejemplo, para el primer ejemplo no sería válido definir el intervalo [1, 7] porque incluiría el rango [4, 5] el cual no
se encuentra incluído entre los originales."""


def menor_conjunto_intervaslos(lista):
    resultado = []
    bolsa = []
    lista.sort(key=lambda x: x[0])
    for inicio, fin in lista:
        if not bolsa:
            bolsa.append(inicio)
            bolsa.append(fin)
        if inicio <= bolsa[-1]:
            if fin > bolsa[-1]:
                bolsa.pop()
                bolsa.append(fin)
            else:
                continue
        else:
            resultado.append(bolsa)
            bolsa = [inicio, fin]
    if bolsa:
        resultado.append(bolsa)
    return resultado


"""La complejidad del algoritmo en cuestion es O(n log n) ya que en este la tarea de mayor complejidad que se realiza es
un ordenamiento comparativo y las demas tareas que se realizan son un recorrido iterativo el cual es lineal y operaciones
de tiempo constante como condicionales y operaciones de listas como pop y append

El algoritmo es greedy ya que su regla es chequear si el elemento actual esta en el intervalo y si lo esta, actualiza acordemente este ultimo.
El optimo local es, hasta el momento tengo un conjunto de intervalos lo mas largos posibles(que incluyan a todos los valores), dando asi una sucesion de la minima cantidad de intervalos"""


def main():
    lista = [[1.3, 2.8], [2.97, 3.2], [0, 1.5], [2.95, 3]]
    print(menor_conjunto_intervaslos(lista))


if __name__ == "__main__":
    main()
