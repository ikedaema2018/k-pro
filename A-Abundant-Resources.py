inputs = [
    '4',
    '4 1 3 3'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = list(map(int, input().split()))

r = [0]
for i in range(len(conditions)):
    r.append(conditions[i] + r[i])

for i in range(1, N + 1):
    result = -1
    for j in range(1, len(r) - i + 1):
        k = j + i - 1
        result = max(r[k] - r[j - 1], result)
    print(result)