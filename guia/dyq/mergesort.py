def merge_sort(arr):
    return merge_sort_rec(arr, 0, len(arr) - 1)


def merge_sort_rec(arr, inicio, fin):
    if inicio == fin:
        return [arr[inicio]]
    medio = (inicio + fin) // 2
    izq = merge_sort_rec(arr, inicio, medio)
    der = merge_sort_rec(arr, medio + 1, fin)
    return merge(izq, der)


def merge(izq, der):
    lista_ordenada = []
    i, j = 0, 0
    while i != len(izq) and j != len(der):
        if izq[i] < der[j]:
            lista_ordenada.append(izq[i])
            i += 1
        else:
            lista_ordenada.append(der[j])
            j += 1
    while i < len(izq):
        lista_ordenada.append(izq[i])
        i += 1
    while j < len(der):
        lista_ordenada.append(der[j])
        j += 1
    return lista_ordenada


def main():
    arreglo = [2, 7, 4, 1, 5, 9]
    print(merge_sort(arreglo))


if __name__ == "__main__":
    main()
