inputs = [
    '4',
    '1 2 3 4'
]


def input():
    return inputs.pop(0)


N = int(input())
H = list(map(int, input().split(' ')))

before = 0
result = 0
trail = 0
for h in H:
    if h > before:
        result = max(result, trail)
        trail = 0
    else:
        trail += 1
    before = h
result = max(result, trail)

print(result)

