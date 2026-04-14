def bolsas(capacidad, productos):
    lista = []
    bolsa = []
    contador = 0
    productos_ordenados = sorted(productos, reverse=True)
    for producto in productos_ordenados:
        contador += producto
        if contador <= capacidad:
            bolsa.append(producto)
            if contador == capacidad or producto == productos_ordenados[-1]:
                lista.append(bolsa)
                contador = 0
                bolsa = []
        else:
            lista.append(bolsa)
            bolsa = [producto]
            contador = producto
    return lista


def main():
    lista = [4, 2, 1, 3, 5]
    print(bolsas(5, lista))


if __name__ == "__main__":
    main()
