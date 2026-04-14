def alternar(arr):
    return alternar_rec(arr, 0, len(arr) - 1)


def alternar_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]
    mitad = (inicio + fin) // 2
    mitad1 = mitad // 2
    mitad2 = mitad * 3 // 4
    izq1 = alternar_rec(arr, inicio, mitad1)
    der1 = alternar_rec(arr, mitad1 + 1, mitad)
    izq2 = alternar_rec(arr, mitad, mitad2)
    der2 = alternar_rec(arr, mitad2 + 1, fin)
    der1, izq2 = izq2, der1


def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    print(alternar(lista))


if __name__ == "__main__":
    main()
