inputs = [
    '5',
    'abaaaaaaaa',
    'oneplustwo',
    'aaaaaaaaba',
    'twoplusone',
    'aaaabaaaaa'
]


def input():
    return inputs.pop(0)
N = int(input())
S = []
for _ in range(N):
    S.append("".join(sorted(input())))

S = sorted(S)
result = 0

before_s = ''
count = 0
for s in S:
    if s == before_s:
        count += 1
    else:
        if count > 1:
            result += count * (count - 1) // 2
        count = 1
        before_s = s
else:
    if count > 1:
        result += count * (count - 1) // 2
print(result)