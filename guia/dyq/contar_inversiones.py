def contar_inversiones(A, B):
    arreglo, inversiones = merge_sort(B)
    return inversiones


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    medio = len(arr) // 2
    izq, inversiones_izq = merge_sort(arr[:medio])
    der, inversiones_der = merge_sort(arr[medio:])
    resultado, inversiones_merge = merge(izq, der)
    total_inversiones = inversiones_izq + inversiones_merge + inversiones_der
    return resultado, total_inversiones


def merge(izq, der):
    inversiones = 0
    resultado = []
    i, j = 0, 0
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
            inversiones += len(izq) - i
    while i < len(izq):
        resultado.append(izq[i])
        i += 1
    while j < len(der):
        resultado.append(der[j])
        j += 1
    return resultado, inversiones


def main():
    b = [6, 8, 7, 2, 1, 5, 3, 4]
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print(contar_inversiones(a, b))


if __name__ == "__main__":
    main()
