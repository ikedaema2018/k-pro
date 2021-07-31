inputs = [
    '3',
]


def input():
    return inputs.pop(0)


N = int(input())

if N <= 1:
    print('0')
else:
    print(N - 1)
