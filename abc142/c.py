inputs = [
    '8',
    '8 2 7 3 4 5 6 1'
]


def input():
    return inputs.pop(0)


N = int(input())
L = list(map(int, input().split(' ')))
h = [0] * N

for x in enumerate(L):
    h[x[1] - 1] = str(x[0] + 1)

print(" ".join(h))