inputs = [
    '2 2 4'
]


def input():
    return inputs.pop(0)


A, B, C = list(map(int, input().split()))
if (A ** 2 + B ** 2) < (C ** 2):
    print('Yes')
else:
    print('No')

