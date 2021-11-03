inputs = [
    '10000000007',
    '2',
    '3',
    '5',
    '7',
    '11'
]


def input():
    return inputs.pop(0)


N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

towns = [0] * 6
towns[0] = N
result = 0
from copy import copy
_towns = copy(towns)

while towns[5] < N:
    a = A if towns[0] >= A else towns[0]
    _towns[0] -= a
    _towns[1] += a

    b = B if towns[1] >= B else towns[1]
    _towns[1] -= b
    _towns[2] += b

    c = C if towns[2] >= C else towns[2]
    _towns[2] -= c
    _towns[3] += c

    d = D if towns[3] >= D else towns[3]
    _towns[3] -= d
    _towns[4] += d

    e = E if towns[4] >= E else towns[4]
    _towns[4] -= e
    _towns[5] += e

    result += 1
    towns = copy(_towns)

print(result)

