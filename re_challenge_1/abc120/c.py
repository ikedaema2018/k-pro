inputs = [
    '0011'
]


def input():
    return inputs.pop(0)

zero = 0
ichi = 0
S = list(input())
for s in S:
    if s == '0':
        zero = zero + 1
    elif s == '1':
        ichi = ichi + 1

print(min(zero, ichi) * 2)
