"""(★) Implementar un algoritmo que, por división y conquista,
permita obtener la parte entera de la raíz cuadrada de un número n, en tiempo O(logn).
Por ejemplo, para n=10 debe devolver 3, y para n=25 debe devolver 5. Justificar la complejidad del algoritmo."""


def obtener_raiz(n):
    return obtener_raiz_rec(n, 0, n)


def obtener_raiz_rec(n, inicio, fin):
    if inicio == fin:
        return inicio
    if 1 <= n <= 3:
        return 1
    medio = (inicio + fin) // 2
    if medio * medio == n or medio * medio == n - 1:
        return medio
    if medio * medio > n:
        return obtener_raiz_rec(n, inicio, medio)
    return obtener_raiz_rec(n, medio + 1, fin)


def main():
    print(obtener_raiz(25))


if __name__ == "__main__":
    main()
