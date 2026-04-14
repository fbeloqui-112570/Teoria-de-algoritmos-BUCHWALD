def juan_el_vago(trabajos):
    if len(trabajos) == 0:
        return []
    if len(trabajos) == 1:
        return [0]

    M_TRABAJOS = [0] * len(trabajos)
    M_TRABAJOS[0] = trabajos[0]
    M_TRABAJOS[1] = max(trabajos[0], trabajos[1])

    for i in range(2, len(trabajos)):
        M_TRABAJOS[i] = max(M_TRABAJOS[i - 1], trabajos[i] + M_TRABAJOS[i - 2])

    reconstruccion = []
    i = len(M_TRABAJOS) - 1

    while i > -1:
        if i == 0 or M_TRABAJOS[i] != M_TRABAJOS[i - 1]:
            reconstruccion.append(i)
            i -= 2
        else:
            i -= 1

    reconstruccion.reverse()
    return reconstruccion


def main():
    trabajos = [100, 5, 50, 1, 1, 200]
    print(juan_el_vago(trabajos))


if __name__ == "__main__":
    main()
