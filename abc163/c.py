inputs = [
    '7',
    '1 2 3 4 5 6'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))
l = [0] * N

for i in range(len(A)):
    a = A[i]
    l[a - 1] += 1
for i in l:
    print(i)