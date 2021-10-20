inputs = [
    '7',
    'beat',
    'vet',
    'beet',
    'bed',
    'vet',
    'bet',
    'beet'
]


def input():
    return inputs.pop(0)


N = int(input())
S = []

for _ in range(N):
    S.append(input())
import collections
result = collections.Counter(S).most_common()
result = sorted(result, key=lambda x: x[0])
result = sorted(result, key=lambda x: x[1], reverse=True)
print(result)
