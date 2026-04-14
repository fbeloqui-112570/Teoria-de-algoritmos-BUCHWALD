def multiplicar(a: int, b: int) -> int:
    if a < 10 or b < 10:
        return a * b

    n = max(len(str(a)), len(str(b)))
    medio = n // 2
    x1, x0 = divmod(a, 10**medio)
    y1, y0 = divmod(b, 10**medio)

    x0y0 = multiplicar(x0, y0)
    x1y1 = multiplicar(x1, y1)
    p = multiplicar((x1 + x0), (y1 + y0))

    return x1y1 * (10 ** (2 * medio)) + (p - x1y1 - x0y0) * 10**medio + x0y0


print(multiplicar(1234, 5678))
