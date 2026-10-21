def cambio(monedas, cambio):
    if not cambio:
        return 0
    OPT = [0] * (cambio + 1)
    OPT[1] = 1
    for i in range(2, cambio + 1):
        max_moneda = 0
        for moneda in monedas:
            if moneda <= i:
                max_moneda = moneda
        OPT[i] = OPT[i - max_moneda] + max_moneda
    return OPT


if __name__ == "__main__":
    print(cambio([1, 2, 3], 5))
