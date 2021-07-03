import math

inputs = [
    '200'
]


def input():
    return inputs.pop(0)


N = int(input())
teika = math.floor(N * 1.08)

if teika == 206:
    print('so-so')
elif teika > 206:
    print(":(")
else:
    print("Yay!")