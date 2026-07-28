import random


def select(S, k):
    if len(S) == 1:
        return S[0]

    ai = random.choice(S)

    S_menos = []
    S_mas = []

    for elem in S:
        if elem < ai:
            S_menos.append(elem)
        elif elem > ai:
            S_mas.append(elem)

    if len(S_menos) == k:
        return ai

    elif len(S_menos) >= k:
        return select(S_menos, k)

    else:
        return select(S_mas, k - 1 - len(S_menos))


if __name__ == "__main__":
    print(select([4, 7, 9, 3, 5, 6], 0))
