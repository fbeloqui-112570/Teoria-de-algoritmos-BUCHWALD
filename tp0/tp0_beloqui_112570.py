import time


def esprimo(n):

    i = 3
    while i <= n**0.5:
        if n % i == 0:
            return False
        i += 2
    return True


def prog():
    t1 = time.time()
    for i in range(11, 1000000, 10):
        if esprimo(i) and esprimo(i + 2) and esprimo(i + 6) and esprimo(i + 8):
            print(i, i + 2, i + 6, i + 8)
    t2 = time.time()
    print(t2 - t1)


prog()
