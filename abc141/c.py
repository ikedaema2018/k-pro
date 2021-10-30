inputs = [
    '6 3 4',
    '3',
    '1',
    '3',
    '2'
]


def input():
    return inputs.pop(0)


N, K, Q = map(int, input().split(' '))
result = [0] * N

for _ in range(Q):
    w = int(input())
    result[w - 1] += 1

result = map(lambda a: 'Yes' if (K - Q + a) > 0 else 'No', result)
for r in result:
    print(r)