inputs = [
    '45 200',
]


def input():
    return inputs.pop(0)

A, B = list(map(int, input().split()))
hiritu = A / 100
print(B * hiritu)