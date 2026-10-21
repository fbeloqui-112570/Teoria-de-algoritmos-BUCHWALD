def sistema_energetico_greedy(lista: list[tuple[int, int]]):
    resultado = []
    lista.sort(key=lambda x: x[0] / x[1], reverse=True)
