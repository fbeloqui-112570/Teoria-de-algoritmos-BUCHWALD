def potencia(b, n):
    if n == 0:
        return 1
    if n == 1:
        return b
    mitad = n // 2
    pot_mitad = potencia(b, mitad)
    imparidad = 1
    if n % 2 == 1:
        imparidad = b
    return pot_mitad * pot_mitad * imparidad


def main():
    print(potencia(3, 3))


if __name__ == "__main__":
    main()
