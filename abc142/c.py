inputs = [
    '8',
    '8 2 7 3 4 5 6 1'
]


def input():
    return inputs.pop(0)


N = int(input())
L = list(map(int, input().split(' ')))
h = {}

for x in enumerate(L):
    h[str(x[1])] = str(x[0] + 1)

result = []
for i in range(N):
    result.append(h[str(i + 1)])
print(" ".join(result))