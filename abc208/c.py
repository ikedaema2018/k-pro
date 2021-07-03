inputs = [
    '20',
    '7 8 1 1 4 9 9 6 8 2 4 1 1 9 5 5 5 3 6 4'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = list(map(int, input().split()))
result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if conditions[i] != conditions[j]:
            result += 1

print(result)