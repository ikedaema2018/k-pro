inputs = [
    '10',
    'aabbbbaaca',
]


def input():
    return inputs.pop(0)


N = int(input())
S = list(input())

before = ''
result = 0
for s in S:
    if before != s:
        result += 1
    before = s

print(result)

