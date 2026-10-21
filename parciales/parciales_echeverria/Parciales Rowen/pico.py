def pico(arr):
    return pico_rec(0, len(arr) - 1, arr)


def pico_rec(inicio, fin, arr):
    if inicio >= fin:
        return arr[inicio]
    mitad = (inicio + fin) // 2
    if arr[mitad - 1] < arr[mitad] > arr[mitad + 1]:
        return arr[mitad]
    if arr[mitad + 1] > arr[mitad]:
        return pico_rec(mitad + 1, fin, arr)
    return pico_rec(inicio, mitad, arr)


if __name__ == "__main__":
    print(
        pico(
            [
                1,
                3,
                5,
                7,
                4,
                2,
            ]
        )
    )
