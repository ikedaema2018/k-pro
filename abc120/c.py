inputs = [
    '0011'
]


def input():
    return inputs.pop(0)


S = list(input())
count_0 = 0
count_1 = 0
for c in S:
    if c == '0':
        count_0 += 1
    else:
        count_1 += 1
print(min(count_0, count_1) * 2)