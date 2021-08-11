inputs = [
    '6174 100000'
]


def input():
    return inputs.pop(0)


N, K = map(int, input().split(' '))
n = N
for _ in range(K):
    ln = list(str(n))
    ask = int("".join(sorted(ln)))
    desk = int("".join(sorted(ln, reverse=True)))
    n = desk - ask
    if len(str(n)) == 1:
        break

print(n)