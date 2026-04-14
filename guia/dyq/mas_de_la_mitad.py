def mas_de_la_mitad(arr):
    elemento = mas_de_la_mitad_rec(arr, 0, len(arr) - 1)
    return arr.count(elemento) > (len(arr) // 2)


def mas_de_la_mitad_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]
    mitad = (inicio + fin) // 2
    izq = mas_de_la_mitad_rec(arr, inicio, mitad)
    der = mas_de_la_mitad_rec(arr, mitad + 1, fin)
    if izq == der:
        return izq
    else:
        cant_izq = contar(arr, izq, inicio, fin)
        cant_der = contar(arr, der, inicio, fin)
        if cant_izq > cant_der:
            return izq
        return der


def contar(arr, elemento, inicio, fin):
    contador = 0
    for i in range(inicio, fin + 1):
        if arr[i] == elemento:
            contador += 1
    return contador


def main():
    lista = [1, 2, 3, 1, 1, 1]
    print(mas_de_la_mitad(lista))


if __name__ == "__main__":
    main()
