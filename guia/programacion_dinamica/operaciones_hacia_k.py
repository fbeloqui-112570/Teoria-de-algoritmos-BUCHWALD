def operaciones(k):
    if k == 0:
        return []
    if k == 1:
        return [1]
    memo = [0] * (k + 1)
    memo[0] = 0
    memo[1] = 1
    for i in range(2, k + 1):
        if i % 2 == 0:
            memo[i] = min(memo[i // 2] + 1, memo[i - 1] + 1)
        else:
            memo[i] = memo[i - 1] + 1
    return reconstruccion(memo)


def reconstruccion(memo):
    lista = []
    i = len(memo) - 1
    while i > -1:
        if i == 0:
            break
        if i % 2 == 0:
            if memo[i // 2] < memo[i]:
                lista.append("por2")
                i = i // 2
        else:
            lista.append("mas1")
            i -= 1
    lista.reverse()
    return lista


def main():
    memo = operaciones(10)
    print(memo)


if __name__ == "__main__":
    main()
