inputs = [
    '3 4 5'
]


def input():
    return inputs.pop(0)


conditions = list(map(int, input().split()))
result = 0
for i in range(0, 3):
    for j in range(i + 1, 3):
        result = max(conditions[i] + conditions[j], result)

print(result)

