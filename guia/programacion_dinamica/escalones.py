def escalones(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    M_ESC = [0] * (n + 1)
    M_ESC[0] = 1
    M_ESC[1] = 1
    M_ESC[2] = 2

    for i in range(3, n + 1):
        M_ESC[i] = M_ESC[i - 1] + M_ESC[i - 2] + M_ESC[i - 3]
    return M_ESC[n]


def main():
    print(escalones(1))


if __name__ == "__main__":
    main()
