inputs = [
    '3',
    '5 6 3 8',
    '5 100 8'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

result = 0
for i in reversed(range(len(B))):
    minus_a_1 = B[i] if A[i + 1] - B[i] >= 0 else A[i + 1]
    B[i] -= minus_a_1
    minus_a_0 = B[i] if A[i] - B[i] >= 0 else A[i]
    A[i] -= minus_a_0
    result = result + minus_a_0 + minus_a_1
print(result)