# https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a
inputs = [
    '7 5',
    '2',
    '1',
    '1',
    '3',
    '2',
    '1',
    '2',
    '-1',
    '3',
    '2',
    '-3'
]


def input():
    return inputs.pop(0)


n, m = list(map(int, input().split()))
towns = [0]
for i in range(n - 1):
    towns.append(towns[i] + int(input()))
travels = []
for _ in range(m):
    travels.append(int(input()))


current = 0
result = 0
for a in travels:
    nxt = a + current
    result += abs(towns[nxt] - towns[current])
    current = nxt
print(result % 100000)


