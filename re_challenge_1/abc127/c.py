inputs = [
    '100000 1',
    '1 100000'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))
l = 0
r = N

for _ in range(M):
    L, R = map(int, input().split(' '))
    l = max(l, L)
    r = min(r, R)
print(max(r - l + 1, 0))

