inputs = [
    10,
    10
]


def input():
    return inputs.pop(0)


N = int(input())
K = int(input())

result = 1
for _ in range(N):
    if (result * 2) > (result + K):
        result = result + K
    else:
        result = result * 2

print(result)