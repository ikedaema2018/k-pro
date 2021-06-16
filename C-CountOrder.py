from itertools import permutations

inputs = [
    '3',
    '1 2 3',
    '1 2 3',
]


def input():
    return inputs.pop(0)


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

p = None
q = None
i = 0
for group in permutations(range(1, N + 1), N):
    if P == list(group):
        p = i
    if Q == list(group):
        q = i
    if p is not None and q is not None:
        break
    i += 1

print(abs(p - q))
