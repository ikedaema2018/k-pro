inputs = [
    '2 5',
    '4 9',
    '2 4'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))
ab_s = [list(map(int, input().split(' '))) for _ in range(N)]
sorted_ab_s = sorted(ab_s, key=lambda ab: ab[0])

result = 0
m = 0
for a, b in sorted_ab_s:
    buy_count = min(b, M - m)
    result += (a * buy_count)
    m += buy_count
    if m >= M:
        break
print(result)
