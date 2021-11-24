inputs = [
    '3',
    '2 8 4'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))

result = 0
for i in range(1, N):
    for j in range(0, i):
        a = (A[i] - A[j]) ** 2
        result += a

print(result)