def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    MEMO = [0] * (n + 1)
    MEMO[0] = 1
    MEMO[1] = 1
    for i in range(2, n + 1):
        MEMO[i] = MEMO[i - 1] + MEMO[i - 2]
    return MEMO[n]


"""Complejidad: Dado que estamos iterando todos los numeros hasta n una unica vez y los guardamos en una lista, la complejidad espacial y temporal del algoritmo es O(n)"""


def main():
    print(fibonacci(5))


if __name__ == "__main__":
    main()
