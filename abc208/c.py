from functools import reduce

inputs = [
    '20',
    '7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = list(map(int, input().split()))
conditions.sort()
result = int(N * (N - 1) / 2)
duplicates = [0]

before = -1
duplicate = 1
for i in conditions:
    if i == before:
        duplicate += 1
    else:
        if duplicate > 1:
            duplicates.append(duplicate)
            duplicate = 1
    if i == conditions[-1] and duplicate > 1:
        conditions.append(duplicate)
    before = i

print(int(result - reduce(lambda x, y: x + (y * (y - 1) / 2), duplicates)))
