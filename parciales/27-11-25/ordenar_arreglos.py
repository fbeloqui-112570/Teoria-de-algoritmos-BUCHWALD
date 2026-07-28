"""Implementar un algoritmo de división y conquista que reciba un arreglo de K arreglos/listas ordenadas, cada una de H elementos

(es decir, en total hay n = K*H elementos) y devuelva un arreglo con todos los elementos, ya ordenados. El algoritmo debe utilizar la

información del enunciado para considerarse aprobable. NO utilizar un heap para resolver el problema, se está evaluando división y

conquista.

Una vez implementado, puede que no sea posible utilizar el Teorema Maestro para calcular su complejidad. Explicar por qué es el caso.

Dar cuál sería la complejidad con una breve justificación (no es necesario hacer una demostración). En caso que tu implementación sí

permita calcular su complejidad con el Teorema Maestro, recomendamos revisar que esté bien hecho y, si lo está, dar su complejidad

dada por el teorema."""


def ordenar_arreglos(arreglos):
    return ordenar_arreglos_rec(0, len(arreglos) - 1, arreglos)


def ordenar_arreglos_rec(inicio, fin, arreglos):
    if inicio == fin:
        return arreglos[inicio]
    mitad = (inicio + fin) // 2
    izq = ordenar_arreglos_rec(inicio, mitad, arreglos)
    der = ordenar_arreglos_rec(mitad + 1, fin, arreglos)
    return merge(izq, der)


def merge(izquierda, derecha):
    resultado = []
    i, j = 0, 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado


if __name__ == "__main__":
    ejemplo_test = [[1, 9, 12], [2, 5, 8], [0, 4, 11], [3, 6, 7]]
    print(ordenar_arreglos(ejemplo_test))
